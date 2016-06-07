using System;

[System.Serializable]
public class RegisterAndLoginMessageFromServer : BaseMessage {
	// Sequence id
	public int sequence_id;
	// Username
	public string name;
	// Password
	public string password;
	// Success
	public bool success;
	// Message
	public string message;
}
