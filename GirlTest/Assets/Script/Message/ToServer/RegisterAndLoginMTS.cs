using System;

[System.Serializable]
public class RegisterAndLoginMessageToServer : BaseMessage {
	// Name
	public string name;
	// Password
	public string password;
	// Sequence id
	public int sequence_id;

	public RegisterAndLoginMessageToServer(int message_type, int target_type, string name, string password, int sequence_id):base(message_type, target_type) {
		this.name = name;
		this.password = password;
		this.sequence_id = sequence_id;
	}
}
