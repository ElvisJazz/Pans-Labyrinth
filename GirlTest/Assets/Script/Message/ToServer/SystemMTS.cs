using System;

[System.Serializable]
public class SystemMessageToServer : BaseMessage {
	// Name
	public string name;
	// Password
	public string password;

	public SystemMessageToServer(int message_type, int target_type, string name, string password, int sequence_id):base(message_type, target_type, sequence_id) {
		this.name = name;
		this.password = password;
	}
}
