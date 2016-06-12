using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;

public class WeaponInfoController : MonoBehaviour {
	[System.Serializable]
	public struct WeaponDetail{
		public string name;
		public int id;
		public int currentAmountInGun;
		public int currentAmountInBag;

		public WeaponDetail(string name, int id, int currentAmountInGun, int currentAmountInBag){
			this.name = name;
			this.id = id;
			this.currentAmountInGun = currentAmountInGun;
			this.currentAmountInBag = currentAmountInBag;
		}
	}
	// All weapon prefabs and names
	public string[] PrefabNames;
	public GameObject[] Prefabs;
	public GameObject[] PrefabImgs;
	Dictionary<string, GameObject> PrefabsDic;
	Dictionary<string, GameObject> PrefabsImgDic;
	// Default selected weapon image
	public GameObject DefaultImg;
	// Weapon selected view content
	public Transform ImgContent;
	// Weapon info text
	public Text WeaponInfoText;
	// Text of the amount of bullets in current gun
	public Text GunBulletText;
	// Text of the amount of bullets of current gun in the bag
	public Text BagBulletText;
	// Weapon pos
	public Transform WeaponPos;
	// Time of displaying information
	public float DisplayTime = 2f;
	// Weapon info
	public GameObject WeaponInfo;
	// Weapon container view
	public GameObject WeaponContainer;
	// Current weapon in bag
	Dictionary<string, WeaponDetail> weaponsInBag = null;
	// Visibility of weapon info 
	bool isVisible = false;
	// Visibility of weapon container
	public static bool isContainerVisible = false;
	// Has displayed information
	bool hasDisplay = false;
	// Current time of displaying information
	float currentTime = 0;
	// Current held weapon and controller
	GameObject currentWeapon = null;
	WeaponController currentWeaponController = null;

	// Awake
	void Awake(){
		// Init weapons in bag
		weaponsInBag = new Dictionary<string, WeaponDetail> ();
//		WeaponDetail detail;
//		detail.name = "FAL";
//		detail.currentAmountInBag = 240;
//		detail.currentAmountInGun = 40;
//		weaponsInBag.Add("FAL", detail);
//		//weaponsInBag.Add("Thumper", detail);
//		weaponsInBag.Add("Spas-12", detail);
//		weaponsInBag.Add("M1911", detail);
	}

	// Use this for initialization
	void Start () {
		PrefabsDic = new Dictionary<string, GameObject> ();
		PrefabsImgDic = new Dictionary<string, GameObject> ();
		// Init prefabs
		for (int i = 0; i < PrefabNames.Length; i++) {
			PrefabsDic.Add (PrefabNames [i], Prefabs [i]);
			PrefabsImgDic.Add(PrefabNames [i], PrefabImgs [i]);
		}
		// Select default weapon
//		WeaponSelector selector = DefaultImg.GetComponent<WeaponSelector> ();
//		selector.OnSelect (null);
//		SelectNewWeapon("FAL");

		SetWeaponInfoVisible (false);
		SetWeaponContainerVisible (false);
	}
	
	// Update is called once per frame
	void Update () {
		if (isVisible) {
			UpdateWeaponAmountInfo ();
			// Whether set weapon container visible
			if (Input.GetKey (KeyCode.B) && !isContainerVisible) {
				// Set mouse cursor visible
				Cursor.visible = true;
				SetWeaponContainerVisible (true);
			} else if (Input.GetKeyUp (KeyCode.B)) {
				// Set mouse cursor invisible
				Cursor.visible = false;
				SetWeaponContainerVisible (false);
			}
		}
		// Whether to reset diplay info
		if (hasDisplay) {
			ResetInfoText ();
		}

	}

	// Set visibility of weapon info
	public void SetWeaponInfoVisible(bool visible){
		if (!visible || currentWeapon != null) {
			WeaponInfo.SetActive (visible);
		}

		isVisible = visible;
	}

	// Set visibility of weapon container
	void SetWeaponContainerVisible(bool visible){
		WeaponContainer.SetActive(visible);
		isContainerVisible = visible;
	}

	// Update weapon amount info
	void UpdateWeaponAmountInfo(){
		if(currentWeaponController != null){
			GunBulletText.text = currentWeaponController.AmountOfBulletsInGun + "/" + currentWeaponController.MaxAmountOfBulletsInGun;
			BagBulletText.text = currentWeaponController.AmountOfBulletsInBag + "/" + currentWeaponController.MaxAmountOfBulletsInBag;
		}
	}

	// Select new weapn
	public void SelectNewWeapon(string weaponName){
		if(weaponsInBag.ContainsKey(weaponName)){
			// Remove current weapon
			if (currentWeapon != null) {
				WeaponDetail detail = weaponsInBag [currentWeaponController.WeaponName];
				// Update previous detail info
				detail.currentAmountInGun = currentWeaponController.AmountOfBulletsInGun;
				detail.currentAmountInBag = currentWeaponController.AmountOfBulletsInBag;
				weaponsInBag [currentWeaponController.WeaponName] = detail;
				// Destroy
				currentWeapon.SetActive(false);
				Destroy (currentWeapon);
			}

			WeaponDetail weaponDetail = weaponsInBag [weaponName];
			// Create new weapon
			currentWeapon = Instantiate(PrefabsDic[weaponName]) as GameObject;
			// Add new weapon to the weapon position
			currentWeapon.transform.parent = WeaponPos.transform;
			currentWeapon.transform.localPosition = PrefabsDic [weaponName].transform.position;
			currentWeapon.transform.localRotation = PrefabsDic [weaponName].transform.rotation;
			// Get current weapon information
			currentWeaponController = currentWeapon.GetComponentInChildren<WeaponController>();
			currentWeaponController.AmountOfBulletsInGun = weaponDetail.currentAmountInGun;
			currentWeaponController.AmountOfBulletsInBag = weaponDetail.currentAmountInBag;
		}else{
			ShowInfo ("No weapon selected! Maybe something wrong happend!", false);
		}
	}

	// Add new weapon in bag
	public void AddNewWeaponInBag(WeaponDetail detail){
		if (!weaponsInBag.ContainsKey (detail.name)) {
			// Add image in selected view
			GameObject img = Instantiate(PrefabsImgDic[detail.name]);
			img.transform.parent = ImgContent.transform;
			// Add in bag
			weaponsInBag.Add (detail.name, detail);
		}
		// Set default weapon
		if (weaponsInBag.Count > 0) {
			SelectNewWeapon (detail.name);
		}

	}

	// Show information of weapons
	public void ShowInfo(string info, bool add){
		if (add) {
			WeaponInfoText.text += "\n" + info;
		} else {
			WeaponInfoText.text = info;
		}

		currentTime = 0;
		hasDisplay = true;
	}

	// Reset weaponInfoText
	public void ResetInfoText(){
		currentTime += Time.deltaTime;
		if (currentTime > DisplayTime) {
			WeaponInfoText.text = "";
			hasDisplay = false;
		}
	}

	// Get weapons list
	public ICollection<WeaponDetail> GetWeaponList(){
		return (ICollection<WeaponDetail>)weaponsInBag.Values;
	}

}
