using System;

[System.Serializable]
public class PlayerMessageFromServer : BaseMessage {
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
	// Dead num
	public int dead_num;
	// Level
	public string level;
}
