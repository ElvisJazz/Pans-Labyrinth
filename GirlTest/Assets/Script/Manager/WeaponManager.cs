using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class WeaponManager : MonoBehaviour {

	// Weapon prefabs
	public GameObject[] WeaponPrefabs;
	// Weapon holder prefabs
	public GameObject[] WeaponHolderPrefabs;

	// Create weapons
	public void CreateWeapon(WeaponMessageFromServer wm){
		// The role hasn't take the weapon, just create it 
		foreach (WeaponInfo info in wm.weapon_info_list) {
			if (info.take == 0) {
				Instantiate (WeaponPrefabs [info.type_id], new Vector3 (info.position [0], info.position [1], info.position [2]), Quaternion.identity);
			} 
			// The role has taken the weapon
			else {
				GameObject infoManager = GameObject.Find ("InfoManager");
				if (infoManager != null) {
					WeaponInfoController.WeaponDetail weaponDetail = new WeaponInfoController.WeaponDetail (info.name, info.current_bullets_in_gun, info.current_bullets_in_bag);
					WeaponInfoController weaponInfoController = infoManager.GetComponent<WeaponInfoController> ();
					weaponInfoController.AddNewWeaponInBag (weaponDetail);
				}
			}
		}
	}

}
