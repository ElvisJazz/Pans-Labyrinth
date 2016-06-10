using System;
using UnityEngine;

[System.Serializable]
public class EnemyMessageToServer : BaseMessage {
	// Enemy id
	public int enemy_id;
	// Health
	public int health;
	// Position
	public float[] position;

	public EnemyMessageToServer(int message_type, int target_type, int enemy_id, Vector3 position, int health):base(message_type, target_type) {
		this.position = new float[3]{position.x, position.y, position.z};
		this.health = health;
		this.enemy_id = enemy_id;
	}
}
