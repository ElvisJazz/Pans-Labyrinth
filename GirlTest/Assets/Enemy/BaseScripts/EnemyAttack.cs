//
// Control enemy attack as base class
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using System.Collections;

[RequireComponent(typeof(Animator))]

public class EnemyAttack : MonoBehaviour {
	// Hurt amount
	public int HurtAmount = 10;
	// Animator
	protected Animator anim;
	// Goblin mover script
	protected EnemyMover mover;
	// Goblin state script
	protected EnemyState state;
	// Player health controller
	protected PlayerHealth playerHealth;
	// Is set attack state
	protected bool isSetAttack = false;
	// Is player in attack range
	protected bool isInAttackRange = false;

	// Use this for initialization
	void Start () {
		// Get goblin state script
		state = GetComponent<EnemyState>();
		// Get goblin mover script
		mover = GetComponent<EnemyMover>();
		// Get goblin animator
		anim = GetComponent<Animator>();

		// Get player health script
		GameObject playerObject= GameObject.Find("Player");
		if(playerObject != null)
		{
			playerHealth = playerObject.GetComponent<PlayerHealth>();
		}
		else {
			Debug.Log("Cannot find PlayerHealth script");
		}
	}
	
	// Update is called once per frame
	void Update () {
		ResetAttackState ();
	}

	// Check collider
	void OnTriggerStay(Collider other){
		if (other.gameObject.name == "Player" && state.Active) {
			isInAttackRange = true;
			Attack (other.gameObject.transform.position);
		}
	}

	void OnTriggerExit(Collider other){
		if (other.gameObject.name == "Player" && state.Active) {
			isInAttackRange = false;
		}
	}

	// Attack
	virtual protected void Attack(Vector3 pos){
		
	}

	// Reset isSetAttack
	virtual protected void ResetAttackState(){
		
	}
		
	// Check attack whether hurt the player
	public void CheckHurt(){
		if (isInAttackRange) {
			playerHealth.GetHurt (HurtAmount);
		}
	}


}
