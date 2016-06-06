using System;
using UnityEngine;
using LitJson;

public class Dispatcher
{
	public static void dispatcher (JsonData data)
	{
		if ((int)data ["target_type"] == MessagePacker.TargetType.PLAYER.GetHashCode ()) {
			HandlePlayerMessaget (data);
		}else if ((int)data ["target_type"] == MessagePacker.TargetType.ENEMY.GetHashCode()){
			HandleEnemyMessaget (data);
		}else if ((int)data ["target_type"] == MessagePacker.TargetType.WEAPON.GetHashCode()){
			HandleWeaponMessaget (data);
		}
	}

	// Handle player messaget
	public static void HandlePlayerMessaget (JsonData data){
		if ((int)data ["message_type"] == MessagePacker.Type.UPDATE.GetHashCode()){
			
		}
	}

	// Handle enmey messaget
	public static void HandleEnemyMessaget (JsonData data){
		if ((int)data ["message_type"] == MessagePacker.Type.CREATE.GetHashCode ()) {
			WeaponSpawner spawner = GameObject.Find ("WeaponSpawner").GetComponent<WeaponSpawner> ();
			spawner.CreateWeapons (data);
		}else if((int)data ["message_type"] == MessagePacker.Type.UPDATE.GetHashCode()){
			
		}
	}

	// Handle weapon messaget
	public static void HandleWeaponMessaget (JsonData data){
		
		if ((int)data ["message_type"] == MessagePacker.Type.CREATE.GetHashCode ()) {
			
		} else if ((int)data ["message_type"] == MessagePacker.Type.UPDATE.GetHashCode ()){
			
		}
	}
}

