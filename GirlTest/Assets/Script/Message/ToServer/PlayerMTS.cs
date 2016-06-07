using System;

[System.Serializable]
public class PlayerMessageToServer : BaseMessage {
	// Player id
	public int player_id;
	// Positon
	public float[] position;
	// Health
	public int health;
	// Experience
	public int experience;
}
