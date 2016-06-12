using System;

[System.Serializable]
public class BaseMessage {
	// End mark
	public const string END_MARK = "/$/";
	// Message type
	public int message_type;
	// Message target type
	public int target_type;
	// Sequence id
	public int sequence_id;

	public BaseMessage(int message_type, int target_type, int sequence_id=0){
		this.message_type = message_type;
		this.target_type = target_type;
		this.sequence_id = sequence_id;
	}

	public BaseMessage(){
	}
}
