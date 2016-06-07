using System;

[System.Serializable]
public class EnemyMessageToServer : BaseMessage {
	// Enemy id
	public int enemy_id;
	// Health
	public int health;
	// Position
	public float[] position;
}
