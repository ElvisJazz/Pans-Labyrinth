﻿//
// Control motion of enmey as base class
// 
// 2016/05/06 Elvis Jia
//
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

[RequireComponent(typeof(Animator))]

public class EnemyMover : MonoBehaviour {
	// Speed
	public float Speed = 5f;
	// Animator
	Animator animator = null;
	// State script
	EnemyState enemyState= null;
	// Routine
	List<Position> routine = null;
	public List<Position> Routine {
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
		enemyState = GetComponent<EnemyState> ();
	}

	void Update() {
		if (enemyState.Run) {
			RunToTarget ();
		}
	}

	// Turn to the target
	public void TurnToTarget (Vector3 pos)
	{
		transform.LookAt (pos);
	}

	// Run towards to target
	public bool RunToTarget(){
		if (routine != null && routine.Count > 0) {
			Vector3 pos = new Vector3 (routine [0].x, routine [0].y, routine [0].z);
			if (pos == transform.position) {
				routine.RemoveAt (0);
				if (routine.Count > 0)
					pos = new Vector3 (routine [0].x, routine [0].y, routine [0].z);
				else
					return true;
			}

			TurnToTarget (pos);
			// Set run state
			animator.SetFloat ("Speed", Speed);
			// Set position
			transform.position = Vector3.MoveTowards(transform.position, pos, Speed * Time.fixedDeltaTime);
		} else {
			animator.SetFloat ("Speed", 0);
		}
		return false;
	}
}
