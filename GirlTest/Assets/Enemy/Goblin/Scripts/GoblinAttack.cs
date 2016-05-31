//
// Control goblin attack
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using System.Collections;

[RequireComponent(typeof(Animator))]

public class GoblinAttack : EnemyAttack {
	// Attack type
	protected string[] attackType = {"Attack1", "Attack2", "Attack3"};

	// Animator state
	static int combatIdleState = Animator.StringToHash("Base Layer.Goblin_combat_idle");
	static int attackState1 = Animator.StringToHash("Base Layer.Attack1");
	static int attackState2 = Animator.StringToHash("Base Layer.Attack2");
	static int attackState3 = Animator.StringToHash("Base Layer.Attack3");

	// Attack
	override protected void Attack(Vector3 pos){
		mover.TurnToTarget (pos);
		anim.SetTrigger ("Combat_idle");
		if (playerHealth.Health>0 && !isSetAttack && anim.GetCurrentAnimatorStateInfo (0).fullPathHash == combatIdleState && !anim.IsInTransition(0)) {
			Random.seed = Mathf.CeilToInt(Time.time * 100f);
			int type = Random.Range (0, attackType.Length);
			anim.SetTrigger (attackType [type]);
			isSetAttack = true;
		}
	}

	// In order to avoid to set attack trriger more than one time when it's in battle_idle state
	override protected void ResetAttackState(){
		AnimatorStateInfo stateInfo = anim.GetCurrentAnimatorStateInfo(0);
		if (stateInfo.fullPathHash == attackState1 ||
			stateInfo.fullPathHash == attackState2 ||
			stateInfo.fullPathHash == attackState3) {
			isSetAttack = false;
			return;
		}
	}
}
