using System;
using System.Collections.Generic;


[Serializable]
public struct Position{
	public int x;
	public int y;
	public int z;
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
}

[Serializable]
public class EnemyMessageFromServer : BaseMessage {
	public EnemyInfo[] enemy_info_list;

}
