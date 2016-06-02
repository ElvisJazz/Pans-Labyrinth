using System.Text;
using System.Collections;
using System.Collections.Generic;
using System;
using LitJson;

public class MessagePacker {
	public enum Type{
		REGISTER = 0,
		LOGIN = 1,
		LOGOUT = 2,
		CREATE = 3,
		UPDATE = 4,
		RUN = 5, 
		ATTACK = 6,
		SAVE = 7
	}

	public enum TargetType{
		PLAYER = 0,
		ENEMY = 1,
		WEAPON = 2,
		SYSTEM = 3
	}

	public static string pack(Type messageType, TargetType targetType, JsonData jsonData){
		jsonData["message_type"] = messageType.GetHashCode();
		jsonData["target_type"] = targetType.GetHashCode();
		return jsonData.ToJson ();
	}

	public static JsonData unpack(String json){
		return JsonMapper.ToObject (json);
	}
	
}
