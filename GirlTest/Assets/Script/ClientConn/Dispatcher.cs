using System;
using UnityEngine;

public class Dispatcher
{
	public static void dispatcher (string message)
	{
		BaseMessage bm = JsonUtility.FromJson<BaseMessage> (message);
		if (bm.target_type == MessageConstant.TargetType.PLAYER.GetHashCode ()) {
			HandlePlayerMessage (message);
		}else if (bm.target_type == MessageConstant.TargetType.ENEMY.GetHashCode()){
			HandleEnemyMessage (message);
		}else if (bm.target_type == MessageConstant.TargetType.WEAPON.GetHashCode()){
			HandleWeaponMessage (message);
		}else if (bm.target_type == MessageConstant.TargetType.SCENE.GetHashCode()){
			HandleSceneMessage (message);
		}
	}

	// Handle player message
	public static void HandlePlayerMessage (string message){
		PlayerMessageFromServer pm = JsonUtility.FromJson<PlayerMessageFromServer> (message);
		if (pm.message_type == MessageConstant.Type.UPDATE.GetHashCode()){
			PlayerManager.UpdateClientPlayer (pm);
		}
	}

	// Handle enmey message
	public static void HandleEnemyMessage (string message){
		EnemyMessageFromServer em = JsonUtility.FromJson<EnemyMessageFromServer> (message);
		if (em.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {
			EnemyManager manager = GameObject.Find ("EnemySpawner").GetComponent<EnemyManager> ();
			manager.CreateEnemy (em);
		}else if(em.message_type == MessageConstant.Type.UPDATE.GetHashCode()){
			EnemyManager manager = GameObject.Find ("EnemySpawner").GetComponent<EnemyManager> ();
			manager.UpdateEnemy (em);
		}
	}

	// Handle weapon message
	public static void HandleWeaponMessage (string message){
		WeaponMessageFromServer wm = JsonUtility.FromJson<WeaponMessageFromServer> (message);
		if (wm.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {
			WeaponManager manager = GameObject.Find ("WeaponSpawner").GetComponent<WeaponManager> ();
			manager.CreateWeapon (wm);
		} 
	}

	// Handle scene message
	public static void HandleSceneMessage (string message){
		MazeMessageFromServer mm = JsonUtility.FromJson<MazeMessageFromServer> (message);
		if (mm.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {			
			MazeManager.CreateMaze (mm);
		} 
	}
}

