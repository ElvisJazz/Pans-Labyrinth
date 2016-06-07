using System;

[System.Serializable]
public class RegisterAndLoginMessageToServer : BaseMessage {
	// Name
	public string name;
	// Password
	public string password;
	// Sequence id
	public int sequence_id;
}
