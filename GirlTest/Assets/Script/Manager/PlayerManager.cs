using UnityEngine;
using System.Collections;

public class PlayerManager{
	// Player id
	public static int player_id;

	public static void UpdatePlayer(PlayerMessageFromServer pm){
		GameObject player = GameObject.Find ("Player");
		if (player != null) {
			player_id = pm.player_id;
			PlayerHealth healthController = player.GetComponent<PlayerHealth> ();
			PlayerExp expController = player.GetComponent<PlayerExp> ();
			healthController.Health = pm.health;
			healthController.MaxHealth = pm.max_health;
			expController.Exp = pm.experience;
			expController.MaxExp = pm.max_experience;
		}

	}
}
