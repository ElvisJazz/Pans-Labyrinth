using UnityEngine;
using System.Collections;

public class EnemyManager : MonoBehaviour {
	// Enemy prefabs
	public GameObject[] Prefabs;
	// Enemy hashtable, key->enemy_id, value->enemy object
	private Hashtable enemy_table = new Hashtable();

	// Create enemies
	public void CreateEnemy(EnemyMessageFromServer em){
		foreach (EnemyInfo ei in em.enemy_info_list) {
			GameObject enemy = Instantiate (Prefabs [ei.enemy_type], new Vector3(ei.position[0], ei.position[1], ei.position[2]), Quaternion.identity) as GameObject;
			EnemyHealth eHealth = enemy.GetComponent<EnemyHealth> ();
			EnemyMover eMover = enemy.GetComponent<EnemyMover> ();
			EnemyAttack eAttack = enemy.GetComponent<EnemyAttack> ();
			EnemyState eState = enemy.GetComponent<EnemyState> ();
			// Set properties
			eHealth.Health = ei.health;
			eHealth.exp = ei.experience;
			eHealth.MaxHealth = ei.max_health;
			eAttack.HurtAmount = ei.hurt;
			eMover.Routine = ei.target_routine;
			enemy.transform.parent = transform;
			// Set state
			SetState(ei.action_type, eState);
			// Add to table
			enemy_table [ei.enemy_id] = enemy;
		}
	}

	// Update enemies
	public void UpdateClientEnemy(EnemyMessageFromServer em){
		foreach (EnemyInfo ei in em.enemy_info_list) {
			GameObject enemy = enemy_table [ei.enemy_id] as GameObject;
			EnemyMover eMover = enemy.GetComponent<EnemyMover> ();
			EnemyState eState = enemy.GetComponent<EnemyState> ();
			// Set properties
			eMover.Routine = ei.target_routine;
			// Set state
			SetState(ei.action_type, eState);
		}
	}

	// Update server enemy information
	public static void UpdateServerEnemy(){
		EnemyMessageToServer em = new EnemyMessageToServer (MessageConstant.Type.UPDATE.GetHashCode(),MessageConstant.TargetType.ENEMY.GetHashCode (),
		if (lastPM != null && lastPM.CheckEqual(pm)) {
			return;
		}
		lastPM = pm;
		string message = JsonUtility.ToJson (pm);
		ClientSocket.GetInstance ().SendMessage (message+BaseMessage.END_MARK);
	}

	// Set state
	private void SetState(int action_type, EnemyState eState){
		if (action_type == EnemyType.ActionType.ATTACK.GetHashCode()) {
			eState.Attack = true;
			eState.Run = false;
		}else{
			eState.Attack = false;
			eState.Run = true;
		}
	}
}
