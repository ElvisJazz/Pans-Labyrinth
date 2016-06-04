using UnityEngine;
using System.Collections;
using LitJson;

public class WeaponSpawner : MonoBehaviour {

	// Weapon prefabs
	public GameObject[] WeaponPrefabs;
	// Weapon holder prefabs
	public GameObject[] WeaponHolderPrefabs;

	// Create weapon
	public void CreateWeapon(JsonData data){
		// The role hasn't take the weapon, just create it 
		if ((int)data ["take"] == 0) {
			//
			//Instantiate(WeaponPrefabs[data["type_id"]], data
		}
	}
}
