using UnityEngine;
using System.Collections;

public class BloodBlock : MonoBehaviour {

	// How much health value can each blood block pay for
	public int HealthValueWorth = 30;
	// Life time
	public float LifeTime = 8.0f;

	// Start
	void Start(){
		Destroy (this.gameObject, LifeTime);
	}

	// Player get blood
	void OnCollisionEnter(Collision other){
		if (other.gameObject.name == "Player") {
			PlayerHealth playerHealth = other.gameObject.GetComponent<PlayerHealth> ();
			// Audio
			AudioSource audioSource = GetComponent<AudioSource>();
			if (audioSource != null) {
				audioSource.Play ();
			}
			// Add health value
			if (playerHealth != null) {
				playerHealth.AddHealthValue (HealthValueWorth);
				Destroy (this.gameObject);
			}
		}
	}
}
