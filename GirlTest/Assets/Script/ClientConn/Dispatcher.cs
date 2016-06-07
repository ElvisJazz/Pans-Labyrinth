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
		}
	}

	// Handle player messaget
	public static void HandlePlayerMessaget (string message){
		PlayerMessageFromServer pm = JsonUtility.FromJson<PlayerMessageFromServer> (message);
		if (pm.message_type == MessageConstant.Type.UPDATE.GetHashCode()){
			
		}
	}

	// Handle enmey messaget
	public static void HandleEnemyMessaget (string message){
		EnemyMessageFromServer em = JsonUtility.FromJson<EnemyMessageFromServer> (message);
		if (em.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {
			
		}else if(em.message_type == MessageConstant.Type.UPDATE.GetHashCode()){
			
		}
	}

	// Handle weapon messaget
	public static void HandleWeaponMessaget (string message){
		WeaponMessageFromServer wm = JsonUtility.FromJson<WeaponMessageFromServer> (message);
		if (wm.message_type == MessageConstant.Type.CREATE.GetHashCode ()) {
			WeaponSpawner spawner = GameObject.Find ("WeaponSpawner").GetComponent<WeaponSpawner> ();
			spawner.CreateWeapon (wm);
		} else if (wm.message_type == MessageConstant.Type.UPDATE.GetHashCode ()){
			
		}
	}
}

