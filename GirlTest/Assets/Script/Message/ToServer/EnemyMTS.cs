using System;
using UnityEngine;
using System.Collections.Generic;

// This class usually for updateing health or action state (not routine)
[System.Serializable]
public class EnemyMessageToServer : BaseMessage {
	// Enemy id
	public int enemy_id;
	// Health
	public int health;
	// Position
	public float[] position;
	// Next position
	public float[] next_position;

	public EnemyMessageToServer(int message_type, int target_type, int enemy_id, int health, Vector3 position, Position next_position) : base(message_type, target_type) {
		this.position = new float[3]{position.x, position.y, position.z};
		this.next_position = new float[3]{next_position.x, next_position.y, next_position.z};
		this.health = health;
		this.enemy_id = enemy_id;
	}
}

// This class usually for updateing routine
[System.Serializable]
public struct ServerEnemyMessage{
	// Enemy id
	public int enemy_id;
	// Health
	public int health;
	// Position
	public float[] position;
	// Next position
	public float[] next_position;

	public ServerEnemyMessage(int enemy_id, int health, Position position, Position next_position) {
		this.position = new float[3]{position.x, position.y, position.z};
		this.next_position = new float[3]{next_position.x, next_position.y, next_position.z};
		this.health = health;
		this.enemy_id = enemy_id;
	}
}

// This class usually for updateing routine
[System.Serializable]
public class EnemyListMessageToServer : BaseMessage {
	public List<ServerEnemyMessage> enemy_info_list = new List<ServerEnemyMessage>();

	public EnemyListMessageToServer(int message_type, int target_type) : base(message_type, target_type){

	}
}
