//
// Control motion of enmey as base class
// 
// 2016/05/06 Elvis Jia
//
using UnityEngine;
using System.Collections;

[RequireComponent(typeof(Animator))]

public class EnemyMover : MonoBehaviour {
	// Speed
	public float Speed = 5.0f;
	// Animator
	Animator animator = null;
	// Routine
	Position[] routine;
	public Position[] Routine {
		get {
			return routine;
		}
		set {
			routine = value;
		}
	}

	// Use this for initialization
	void Start () {
		animator = GetComponent<Animator> ();
	}

	// Turn to the target
	public void TurnToTarget (Vector3 pos)
	{
		transform.LookAt (pos);
	}

	// Run towards to target
	public bool RunToTarget(Vector3 pos){
		TurnToTarget (pos);
		if (pos == transform.position) {
			animator.SetTrigger ("Idle");
			return true;
		}
		// Set run state
		animator.SetTrigger ("Run");
		// Set position
		transform.position += Vector3.forward * Speed * Time.fixedTime;
		return false;
	}
}
