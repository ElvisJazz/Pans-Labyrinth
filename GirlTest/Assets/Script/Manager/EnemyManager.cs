using UnityEngine;
using System.Collections;
using System.Collections.Generic;

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
			eHealth.EnemyId = ei.enemy_id;
			eAttack.HurtAmount = ei.hurt;
			EnemyAttack.HurtDistanceSquare = ei.attack_distance_square;
			eMover.EnemyId = ei.enemy_id;
			SetRoutine(eMover.Routine, ei.target_routine, ei.action_type);
			enemy.transform.parent = transform;
			// Set state
			SetState(ei.action_type, eState);
			// Add to table
			enemy_table [ei.enemy_id] = enemy;
		}
	}

	// Update enemies of client
	public void UpdateClientEnemy(EnemyMessageFromServer em){
		foreach (EnemyInfo ei in em.enemy_info_list) {
			GameObject enemy = enemy_table [ei.enemy_id] as GameObject;
			if (enemy != null) {
				EnemyMover eMover = enemy.GetComponent<EnemyMover> ();
				EnemyState eState = enemy.GetComponent<EnemyState> ();
				// Set properties
				SetRoutine (eMover.Routine, ei.target_routine, ei.action_type);
				// Set state
				SetState (ei.action_type, eState);
			}
		}
	}

	// Update server enemy information if the enemy reach the target position or die
	public void UpdateSignleServerEnemy(int enemy_id){
		if(enemy_table.ContainsKey(enemy_id)){
			GameObject enemy = enemy_table [enemy_id] as GameObject;
			EnemyHealth eHealth = enemy.GetComponent<EnemyHealth> ();
			EnemyMover eMover = enemy.GetComponent<EnemyMover> ();
			if (eHealth.Health <= 0)
				enemy_table.Remove (enemy_id);
			Position next_position = new Position(enemy.transform.position); // eMover.Routine.Count > 0 ? eMover.Routine [0] : 
			EnemyMessageToServer em = new EnemyMessageToServer (MessageConstant.Type.UPDATE.GetHashCode (), MessageConstant.TargetType.ENEMY.GetHashCode (), enemy_id, eHealth.Health, enemy.transform.position, next_position);
			string message = JsonUtility.ToJson (em);
			ClientSocket.GetInstance ().SendMessage (message+BaseMessage.END_MARK);
		}
	}

	// Update server enemy information list if the position of player changes 
	public string GetUpdateServerEnemyListMessage(){
		EnemyListMessageToServer elm = new EnemyListMessageToServer (MessageConstant.Type.UPDATE.GetHashCode (), MessageConstant.TargetType.ENEMY.GetHashCode ());
		// Add each enemy info to list of message
		foreach (int enemy_id in enemy_table.Keys) {
			GameObject enemy = enemy_table [enemy_id] as GameObject;
			EnemyHealth eHealth = enemy.GetComponent<EnemyHealth> ();
			EnemyMover eMover = enemy.GetComponent<EnemyMover> ();
			Position position = new Position(enemy.transform.position);
			Position next_position = new Position(enemy.transform.position); // eMover.Routine.Count > 0 ? eMover.Routine [0] : 
			ServerEnemyMessage sm = new ServerEnemyMessage (enemy_id, eHealth.Health, position, next_position);
			elm.enemy_info_list.Add (sm);
		}
		return JsonUtility.ToJson (elm) + BaseMessage.END_MARK;
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

	// Set routine
	private void SetRoutine(List<Position> currentRoutine, List<Position> newRoutine, int action_type){
		if (action_type == EnemyType.ActionType.ATTACK.GetHashCode ()) {
			currentRoutine.Clear ();
			currentRoutine.AddRange (newRoutine);
		} else { //if (currentRoutine.Count > 0 && newRoutine.Count > 0) 
			if (currentRoutine.Count > 0) {
				newRoutine.Insert (0, currentRoutine [0]);
				Position po = currentRoutine [0];
				Debug.Log ("before:" + po.x+"||"+po.y+"||"+po.z);
			}
			currentRoutine.Clear();
			currentRoutine.AddRange(newRoutine);
		}
	}
}
