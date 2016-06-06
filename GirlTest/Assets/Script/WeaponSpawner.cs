using UnityEngine;
using System.Collections;
using LitJson;

public class WeaponSpawner : MonoBehaviour {

	// Weapon prefabs
	public GameObject[] WeaponPrefabs;
	// Weapon holder prefabs
	public GameObject[] WeaponHolderPrefabs;

	// Create weapons
	public void CreateWeapons(JsonData data){
		if (data.IsArray) {
			foreach (IDictionary dic in data) {
				CreateWeapon (dic);
			}
		} else {
			CreateWeapon ((IDictionary)data);
		}
	}

	// Create weapon
	public void CreateWeapon(IDictionary dic){
		// The role hasn't take the weapon, just create it 
		if ((int)dic ["take"] == 0) {
			float[] pos = (float[])dic ["position"];
			Instantiate (WeaponPrefabs [(int)(dic ["type_id"])], new Vector3(pos[0],pos[1], pos[2]), Quaternion.identity);
		} 
		// The role has taken the weapon
		else {
			GameObject infoManager = GameObject.Find ("InfoManager");
			if (infoManager != null) {
				WeaponInfoController.WeaponDetail weaponDetail = new WeaponInfoController.WeaponDetail ((string)dic["name"],(int)dic["currentAmountInGun"], (int)dic["currentAmountInBag"]);
				WeaponInfoController weaponInfoController = infoManager.GetComponent<WeaponInfoController> ();
				weaponInfoController.AddNewWeaponInBag (weaponDetail);
			}
		}
	}
}
