using System;
using UnityEngine;

[System.Serializable]
public class PlayerMessageToServer : BaseMessage {
	// Positon
	public float[] position;
	// Health
	public int health;
	// Experience
	public int experience;
	// Dead num
	public int dead_num;

	public PlayerMessageToServer(int message_type, int target_type, Vector3 position, int health, int experience, int dead_num):base(message_type, target_type) {
		this.position = new float[3]{position.x, position.y, position.z};
		this.health = health;
		this.experience = experience;
		this.dead_num = dead_num;
	}

	public bool CheckEqual(PlayerMessageToServer pm){
		if (Mathf.Abs(this.position[0]-pm.position[0])<=0.1 && Mathf.Abs(this.position[1]-pm.position[1])<=0.1 && Mathf.Abs(this.position[2]-pm.position[2])<=0.1
		   && this.health == pm.health && this.experience == pm.experience)
			return true;
		else
			return false;
	}
}
