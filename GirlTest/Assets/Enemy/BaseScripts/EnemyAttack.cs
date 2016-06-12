//
// Control enemy attack as base class
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using System.Collections;

[RequireComponent(typeof(Animator))]

public class EnemyAttack : MonoBehaviour {
	// Hurt distance
	public static float HurtDistanceSquare = 0.64f;
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
		//ResetAttackState ();
		if(state.Attack)
			Attack (playerHealth.transform.position);
	}

	// Attack
	virtual protected void Attack(Vector3 pos){
		
	}

	// Reset isSetAttack
	virtual protected void ResetAttackState(){
		
	}
		
	// Check attack whether hurt the player
	public void CheckHurt(){
		if (GetDistanceSquare(playerHealth.transform.position, transform.position) <= HurtDistanceSquare) {
			playerHealth.GetHurt (HurtAmount);
		}
	}

	// Get the distance between enemy and player
	public static float GetDistanceSquare(Vector3 pos1, Vector3 pos2){
		return Mathf.Pow (pos1[0]-pos2[0], 2) + Mathf.Pow (pos1 [2]-pos2[2], 2);
	}


}
