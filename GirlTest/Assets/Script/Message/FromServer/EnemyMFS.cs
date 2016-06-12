using System;
using System.Collections.Generic;
using UnityEngine;


[Serializable]
public struct Position{
	public float x;
	public float y;
	public float z;

	public Position(Vector3 pos){
		this.x = pos.x;
		this.y = pos.y;
		this.z = pos.z;
	}

	public Position(float x, float y, float z){
		this.x = x;
		this.y = y;
		this.z = z;
	}
}

[Serializable]
public struct EnemyInfo{
	// Enemy type
	public int enemy_type;
	// Enemy id
	public int enemy_id;
	// Health
	public int health;
	// Max health
	public int max_health;
	// Position
	public float[] position;
	// Hurt
	public int hurt;
	// Experience
	public int experience;
	// Target routine
	public List<Position> target_routine;
	// Action type
	public int action_type;
	// Hurt disatnce square
	public float attack_distance_square;
}

[Serializable]
public class EnemyMessageFromServer : BaseMessage {
	public EnemyInfo[] enemy_info_list;

}
