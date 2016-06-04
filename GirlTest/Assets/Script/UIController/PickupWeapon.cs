using UnityEngine;
using System.Collections;

public class PickupWeapon : MonoBehaviour {
	// Weapon info detail 
	public WeaponInfoController.WeaponDetail WeaponDetail;

	// Pickup
	void OnTriggerEnter(Collider other){
		if (other.gameObject.name == "Player") {
			GameObject infoManager = GameObject.Find ("InfoManager");
			if (infoManager != null) {
				WeaponInfoController weaponInfoController = infoManager.GetComponent<WeaponInfoController> ();
				weaponInfoController.AddNewWeaponInBag (WeaponDetail);
				Destroy (this.gameObject);
			}
		}
	}
		
}
