using System;

[System.Serializable]
public class SystemMessageFromServer : BaseMessage {
	// Sequence id
	public int sequence_id;
	// Success
	public bool success;
	// Message
	public string message;
}
