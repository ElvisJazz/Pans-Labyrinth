using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class WeaponManager : MonoBehaviour {

	// Weapon prefabs
	public GameObject[] WeaponPrefabs;

	// Create weapons
	public void CreateWeapon(WeaponMessageFromServer wm){
		// The role hasn't take the weapon, just create it 
		foreach (WeaponInfo info in wm.weapon_info_list) {
			if (info.take == 0) {
				GameObject weapon = Instantiate (WeaponPrefabs [info.type_id], new Vector3 (info.position [0], info.position [1], info.position [2]), Quaternion.identity) as GameObject;
				WeaponInfoController.WeaponDetail detail = new WeaponInfoController.WeaponDetail ();
				detail.name = info.name;
				detail.id = info.weapon_id;
				detail.currentAmountInGun = info.current_bullets_in_gun;
				detail.currentAmountInBag = info.current_bullets_in_bag;
				weapon.GetComponent<PickupWeapon> ().WeaponDetail = detail;
			} 
			// The role has taken the weapon
			else {
				GameObject infoManager = GameObject.Find ("InfoManager");
				if (infoManager != null) {
					WeaponInfoController.WeaponDetail weaponDetail = new WeaponInfoController.WeaponDetail (info.name, info.weapon_id, info.current_bullets_in_gun, info.current_bullets_in_bag);
					WeaponInfoController weaponInfoController = infoManager.GetComponent<WeaponInfoController> ();
					weaponInfoController.AddNewWeaponInBag (weaponDetail);
				}
			}
		}
	}

	// Update server weapons information
	public static void UpdateServerWeapons(){
		GameObject infoManager = GameObject.Find ("InfoManager");
		WeaponInfoController weaponInfoController = infoManager.GetComponent<WeaponInfoController> ();
		ICollection<WeaponInfoController.WeaponDetail> list = weaponInfoController.GetWeaponList ();

		WeaponListMessageToServer wlm = new WeaponListMessageToServer (MessageConstant.Type.UPDATE.GetHashCode (), MessageConstant.TargetType.WEAPON.GetHashCode ());
		// Add each enemy info to list of message
		foreach (WeaponInfoController.WeaponDetail detail in list) {
			WeaponMessage m = new WeaponMessage (detail.id, 1, detail.currentAmountInGun, detail.currentAmountInBag);
			wlm.weapon_info_list.Add (m);
		}
		string message = JsonUtility.ToJson (wlm) + BaseMessage.END_MARK;
		ClientSocket.GetInstance ().SendMessage (message);
	}
}
