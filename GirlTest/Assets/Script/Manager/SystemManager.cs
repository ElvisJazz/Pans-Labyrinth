using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;
using System.Threading;

public class SystemManager{

	// Check result of login and register
	public static bool CheckResult(int squence_id, MessageConstant.Type type){
		SystemMessageFromServer rl_message = null;
		int i = 0;
		while (rl_message == null && i<=10) {
			rl_message = ClientSocket.GetInstance ().GetSystemMessage (squence_id);
			Thread.Sleep (1000);
			i++;
		}
		if (rl_message == null) {
			MessageTip.SetTip (type + " time out!");  
		} else if (rl_message.success) {
			if (type == MessageConstant.Type.REGISTER) {
				MessageTip.SetTip ("Register success, please login!");  
				return true;
			} else if (type == MessageConstant.Type.LOGIN){
				SceneManager.LoadScene (1);
				return true;
			} else if (type == MessageConstant.Type.SAVE){
				MessageTip.SetTip ("保存成功！");
				return true;
			}
		} else if (rl_message.message != "") {
			MessageTip.SetTip (rl_message.message);  
		}
		return false;
	}

	// Send register and login message
	public static bool SendRegiserAndLoginMessage(MessageConstant.Type type, string username, string password){
		int sequence_id = Mathf.RoundToInt (Time.time * 1000);
		SystemMessageToServer data = new SystemMessageToServer(type.GetHashCode (), MessageConstant.TargetType.SYSTEM.GetHashCode (),
			username, password, sequence_id);
		string message = JsonUtility.ToJson (data);
		ClientSocket.GetInstance ().SendMessage (message+BaseMessage.END_MARK);
		return CheckResult (sequence_id, type);
	}

	// Save
	public static bool Save(){
		// Save player, enemies and weapons information
		PlayerManager.UpdateServerPlayer (true);
		WeaponManager.UpdateServerWeapons ();
		// Send save command and wait for respond
		int sequence_id = Mathf.RoundToInt (Time.time * 1000);
		BaseMessage bm = new BaseMessage (MessageConstant.Type.SAVE.GetHashCode(), MessageConstant.TargetType.SYSTEM.GetHashCode(), sequence_id);
		string message = JsonUtility.ToJson (bm) + BaseMessage.END_MARK;
		ClientSocket.GetInstance ().SendMessage (message);
		return CheckResult (sequence_id, MessageConstant.Type.SAVE);
	}

}
