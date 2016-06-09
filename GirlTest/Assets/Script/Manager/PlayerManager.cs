using UnityEngine;
using System.Collections;

public class PlayerManager{
	// Last information
	private static PlayerMessageToServer lastPM = null;
	// Player health script
	private static PlayerHealth playerHealth = GameObject.Find("Player").GetComponent<PlayerHealth>();
	// Player exp script
	private static PlayerExp playerExp = GameObject.Find("Player").GetComponent<PlayerExp>();
	// Update client player information
	public static void UpdateClientPlayer(PlayerMessageFromServer pm){
		playerHealth.Health = pm.health;
		playerHealth.MaxHealth = pm.max_health;
		playerExp.Exp = pm.experience;
		playerExp.MaxExp = pm.max_experience;
	}

	// Update server player information
	public static void UpdateServerPlayer(){
		PlayerMessageToServer pm = new PlayerMessageToServer (MessageConstant.Type.UPDATE.GetHashCode(),MessageConstant.TargetType.PLAYER.GetHashCode (), playerHealth.transform.position, playerHealth.Health, playerExp.Exp);
		if (lastPM != null && lastPM.CheckEqual(pm)) {
			return;
		}
		lastPM = pm;
		string message = JsonUtility.ToJson (pm);
		ClientSocket.GetInstance ().SendMessage (message+BaseMessage.END_MARK);
	}
}
