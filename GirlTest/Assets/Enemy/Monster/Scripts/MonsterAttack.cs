//
// Control monster attack
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using System.Collections;

[RequireComponent(typeof(Animator))]

public class MonsterAttack : EnemyAttack {
	// Attack type
	protected string[] attackType = {"Attack", "Heavy_attack"};

	// Animator state
	static int combatIdleState = Animator.StringToHash("Base Layer.Monster_combat_idle");
	static int attackState1 = Animator.StringToHash("Base Layer.Attack");
	static int attackState2 = Animator.StringToHash("Base Layer.Heavy Attack");

	// Attack
	override protected void Attack(Vector3 pos){
		mover.TurnToTarget (pos);
		anim.SetTrigger ("Combat_idle");
		if (playerHealth.Health>0 && !isSetAttack && anim.GetCurrentAnimatorStateInfo(0).fullPathHash == combatIdleState && !anim.IsInTransition(0)) {
			Random.seed = Mathf.CeilToInt(Time.time * 100f);
			int type = Random.Range (0, attackType.Length);
			anim.SetTrigger (attackType [type]);
			isSetAttack = true;
		}
	}

	// In order to avoid to set attack trriger more than one time when it's in battle_idle state
	override protected void ResetAttackState(){
		// Get state info
		AnimatorStateInfo stateInfo = anim.GetCurrentAnimatorStateInfo(0);
		if (stateInfo.fullPathHash == attackState1 ||
			stateInfo.fullPathHash == attackState2){
			isSetAttack = false;
			return;
		}
	}
}
