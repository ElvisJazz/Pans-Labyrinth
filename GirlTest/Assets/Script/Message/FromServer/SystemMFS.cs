using System;

[System.Serializable]
public class SystemMessageFromServer : BaseMessage {
	// Success
	public bool success;
	// Message
	public string message;
}
