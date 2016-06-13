using UnityEngine;
using System.Collections;

public class SupplyBlock : MonoBehaviour {
	
	// Player get blood
	void OnCollisionEnter(Collision other){
		if (other.gameObject.name == "Player") {
			// Add bullets
			GameObject infoManager = GameObject.Find ("InfoManager");
			WeaponInfoController weaponInfoController = infoManager.GetComponent<WeaponInfoController> ();
			weaponInfoController.AddFullBullets ();
			// Audio
			AudioSource audioSource = GetComponent<AudioSource>();
			if (audioSource != null) {
				audioSource.Play ();
			}

			Destroy (this.gameObject);
		}
	}
}
