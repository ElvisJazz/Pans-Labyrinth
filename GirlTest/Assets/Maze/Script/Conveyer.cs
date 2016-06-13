using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Conveyer : MonoBehaviour {

	// Next position
	private Vector3 transferPosition;
	public Vector3 TransferPosition{
		get{
			return transferPosition;
		}
		set{
			transferPosition = value;
		}
	}

	// Is in the Conveyer
	private static bool IsInConveyer =  false;
	// Local flag
	private bool flag = false;
	

	// Transfer player to next position
	void OnTriggerEnter (Collider other) {
		if (other.gameObject.name == "Player" && !IsInConveyer) {
			// Transfer
			other.gameObject.transform.position = transferPosition;
			IsInConveyer = true;
			flag = true;
		}
	}

	void OnTriggerExit (Collider other) {
		if (other.gameObject.name == "Player" && IsInConveyer) {
			if (!flag) {
				IsInConveyer = false;
			} else {
				flag = false;
			}
		}
	}
}
