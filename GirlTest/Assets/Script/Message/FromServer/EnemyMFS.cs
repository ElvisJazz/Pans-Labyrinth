using System;

[System.Serializable]
public class EnemyMessageFromServer : BaseMessage {
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
	// Target position
	public float[] target_position;
	// Action type
	public int action_type;

}
