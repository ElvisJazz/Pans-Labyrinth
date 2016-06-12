//
// Control motion of enmey as base class
// 
// 2016/05/06 Elvis Jia
//
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

[RequireComponent(typeof(Animator))]

public class EnemyMover : MonoBehaviour {
	int enemyId;
	public int EnemyId {
		get{
			return enemyId;
		}
		set{
			enemyId = value;
		}
	}
	// Player health controller
	protected PlayerHealth playerHealth;
	// Speed
	public float Speed = 5f;
	// Animator
	Animator animator = null;
	// State script
	EnemyState enemyState= null;
	// Enemy manager
	EnemyManager enemyManager = null;
	// Routine
	List<Position> routine = new List<Position>();
	public List<Position> Routine {
		get {
			return routine;
		}
		set {
			routine = value;
		}
	}
	// Constant positon
	public readonly Vector3 NONE_POSITION = new Vector3(-100,-100,-100); 
	// Current target position
	private Vector3 currentTargetPosition;

	// Use this for initialization
	void Start () {
		currentTargetPosition = NONE_POSITION;
		animator = GetComponent<Animator> ();
		enemyState = GetComponent<EnemyState> ();
		enemyManager = GameObject.Find ("EnemySpawner").GetComponent<EnemyManager> ();
		playerHealth = GameObject.Find ("Player").GetComponent<PlayerHealth> ();
	}

	void Update() {
		if(enemyState.Run)
			RunToTarget ();
		else
			animator.SetFloat ("Speed", 0);
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
			if (routine.Count >1 && pos == transform.position) {
				routine.RemoveAt (0);
				if (routine.Count > 0)
					pos = new Vector3 (routine [0].x, routine [0].y, routine [0].z);
			} else if(routine.Count <= 1 && EnemyAttack.GetDistanceSquare (transform.position, pos) <= EnemyAttack.HurtDistanceSquare-0.1){
				enemyManager.UpdateSignleServerEnemy (enemyId);
				return true;
			}
			TurnToTarget (pos);
			// Set run state
			animator.SetFloat ("Speed", Speed);
			// Set position
			transform.position = Vector3.MoveTowards(transform.position, pos, Speed * Time.deltaTime);
		} else {
			animator.SetFloat ("Speed", 0);
		}
		return false;
	}

	void OnCollisionEnter(Collision other){
		if(other.gameObject.CompareTag("Enemy")){
			EnemyMover enemyMover = other.gameObject.GetComponent<EnemyMover> ();
			// give a way for the enemy which id is less
			if (enemyMover.EnemyId < this.enemyId) {
				//transform.Translate(0f, 0f, 1.0f);
				Position pos = new Position(routine[0].x+0.5f, 0, routine[0].z);
				routine [0] = pos;

			}
				
		}
	}

}
