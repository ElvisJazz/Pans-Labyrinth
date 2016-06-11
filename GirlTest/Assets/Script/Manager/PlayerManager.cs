using UnityEngine;
using System.Collections;

public class PlayerManager{
	// Last information
	private static PlayerMessageToServer lastPM = null;
	// Player health script
	private static PlayerHealth playerHealth = GameObject.Find("Player").GetComponent<PlayerHealth>();
	// Player exp script
	private static PlayerExp playerExp = GameObject.Find("Player").GetComponent<PlayerExp>();
	// Enemy manager script
	private static EnemyManager enemyManager = GameObject.Find("EnemySpawner").GetComponent<EnemyManager>();
	// Update client player information
	public static void UpdateClientPlayer(PlayerMessageFromServer pm){
		playerHealth.Health = pm.health;
		playerHealth.MaxHealth = pm.max_health;
		playerExp.Exp = pm.experience;
		playerExp.MaxExp = pm.max_experience;
	}

	// Update server player information and send current state of all enemies
	public static void UpdateServerPlayer(){
		PlayerMessageToServer pm = new PlayerMessageToServer (MessageConstant.Type.UPDATE.GetHashCode(),MessageConstant.TargetType.PLAYER.GetHashCode (), playerHealth.transform.position, playerHealth.Health, playerExp.Exp);
		if (lastPM != null && lastPM.CheckEqual(pm)) {
			return;
		}
		lastPM = pm;
		// The server will firstly handle state of enemies and then that of player, so it can plan new routines for enemies according to position of the player
		string message = enemyManager.GetUpdateServerEnemyListMessage() + JsonUtility.ToJson (pm) + BaseMessage.END_MARK;
		ClientSocket.GetInstance ().SendMessage (message);

//		string message = "{\"message_type\":4,\"target_type\":1,\"enemy_info_list\":[{\"enemy_id\":0,\"health\":100,\"position\":[-0.007310067303478718,-1.1909863673054133e-7,6.996026515960693]}]}/$/{\"message_type\":4,\"target_type\":0,\"player_id\":0,\"position\":[-0.06982535868883133,5.971529759563055e-8,10.564777374267579],\"health\":100,\"experience\":0}/$/";
//		ClientSocket.GetInstance ().SendMessage (message);
	}
}
