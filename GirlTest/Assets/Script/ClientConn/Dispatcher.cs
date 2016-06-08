using System;
using UnityEngine;

public class Dispatcher
{
	public static void dispatcher (string message)
	{
		BaseMessage bm = JsonUtility.FromJson<BaseMessage> (message);
		if (bm.target_type == MessageConstant.TargetType.PLAYER.GetHashCode ()) {
			HandlePlayerMessaget (message);
		}else if (bm.target_type == MessageConstant.TargetType.ENEMY.GetHashCode()){
			HandleEnemyMessaget (message);
		}else if (bm.target_type == MessageConstant.TargetType.WEAPON.GetHashCode()){
			HandleWeaponMessaget (message);
		}else if (bm.target_type == MessageConstant.TargetType.SCENE.GetHashCode()){
			HandleSceneMessaget (message);
		}
	}

	// Handle player message
	public static void HandlePlayerMessaget (string message){
		PlayerMessageFromServer pm = JsonUtility.FromJson<PlayerMessageFromServer> (message);
		if (pm.message_type == MessageConstant.Type.UPDATE.GetHashCode()){
			PlayerManager.UpdatePlayer (pm);
		}
	}

	// Handle enmey message
	public static void HandleEnemyMessaget (string message){
		EnemyMessageFromServer em = JsonUtility.FromJson<EnemyMessageFromServer> (message);
		if (em.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {
			
		}else if(em.message_type == MessageConstant.Type.UPDATE.GetHashCode()){
			
		}
	}

	// Handle weapon message
	public static void HandleWeaponMessaget (string message){
		WeaponMessageFromServer wm = JsonUtility.FromJson<WeaponMessageFromServer> (message);
		if (wm.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {
			WeaponManager manager = GameObject.Find ("WeaponSpawner").GetComponent<WeaponManager> ();
			manager.CreateWeapon (wm);
		} 
	}

	// Handle scene message
	public static void HandleSceneMessaget (string message){
		MazeMessageFromServer mm = JsonUtility.FromJson<MazeMessageFromServer> (message);
		if (mm.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {			
			MazeManager.CreateMaze (mm);
		} 
	}
}

