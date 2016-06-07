using System;

[System.Serializable]
public class PlayerMessageFromServer : BaseMessage {
	// Player id
	public int player_id;
	// Health
	public int health;
	// Max health
	public int max_health;
	// Experience
	public int experience;
	// Max experience
	public int max_experience;
	// Position
	public float[] position;
}
