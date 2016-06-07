using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class WeaponSpawner : MonoBehaviour {

	// Weapon prefabs
	public GameObject[] WeaponPrefabs;
	// Weapon holder prefabs
	public GameObject[] WeaponHolderPrefabs;

	// Create weapons
	public void CreateWeapon(WeaponMessageFromServer wm){
		// The role hasn't take the weapon, just create it 
		if (wm.take == 0) {
			Instantiate (WeaponPrefabs [wm.type_id], new Vector3(wm.position[0],wm.position[1], wm.position[2]), Quaternion.identity);
		} 
		// The role has taken the weapon
		else {
			GameObject infoManager = GameObject.Find ("InfoManager");
			if (infoManager != null) {
				WeaponInfoController.WeaponDetail weaponDetail = new WeaponInfoController.WeaponDetail (wm.name, wm.current_bullets_in_gun, wm.current_bullets_in_bag);
				WeaponInfoController weaponInfoController = infoManager.GetComponent<WeaponInfoController> ();
				weaponInfoController.AddNewWeaponInBag (weaponDetail);
			}
		}
	}

}
