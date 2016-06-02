using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System;
using LitJson;
using System.Threading;
using UnityEngine.SceneManagement;

public class ButtonController : MonoBehaviour {

	// Register area
	public GameObject RegisterArea;
	// Login area
	public GameObject LoginArea;
	// Register username text
	public Text RegUsernameText;
	// Register username password1
	public GameObject RegPasswordObj1;
	// Register username password2
	public GameObject RegPasswordObj2;
	// Login username text
	public Text LoginUsernameText;
	// Login password text
	public GameObject LoginPasswordObj;
	// Username tip text
	public Text UsernameTipText;
	// Password tip text
	public Text PasswordTipText;

	// Register
	public void OnClickRegister(){
		ClearTips ();
		RegisterArea.SetActive (true);
		LoginArea.SetActive (false);
	}

	// Back
	public void OnClickBack(){
		ClearTips ();
		ClearRegisterInfo ();
		RegisterArea.SetActive (false);
		LoginArea.SetActive (true);
	}

	// Login
	public void OnClickLogin(){
		bool nextOpFlag = true;
		String username = LoginUsernameText.text.Trim ();
		String password = LoginPasswordObj.GetComponent<InputField>().text;
		if (username == "") {
			UsernameTipText.text = "Username shouldn't be null!";
			nextOpFlag = false;
		} else {
			UsernameTipText.text = "";
		}
		if (password == "") {
			PasswordTipText.text = "Password shouldn't be null!";
			nextOpFlag = false;
		} else {
			PasswordTipText.text = "";
		}
		if (!nextOpFlag)
			return;
		// Login option
		JsonData data = new JsonData();
		data["name"] = username;
		data["password"] = password;
		String message = MessagePacker.pack (MessagePacker.Type.LOGIN, MessagePacker.TargetType.SYSTEM, data);
		ClientSocket.GetInstance ().SendMessage (message);
	}

	// RegisterOK
	public void OnClickRegisterOK(){
		bool nextOpFlag = true;
		String username = RegUsernameText.text.Trim ();
		String password1 = RegPasswordObj1.GetComponent<InputField>().text;
		String password2 = RegPasswordObj2.GetComponent<InputField>().text;

		if (username == "") {
			UsernameTipText.text = "Username shouldn't be null!";
			nextOpFlag = false;
		}else {
			UsernameTipText.text = "";
		}
		if (password1 != password2) {
			PasswordTipText.text = "Passwords should be same!";
			nextOpFlag = false;
		} else if (password1 == "") {
			PasswordTipText.text = "Password shouldn't be null!";
			nextOpFlag = false;
		} else {
			PasswordTipText.text = "";
		}
		if (!nextOpFlag)
			return;
		// Register option
		JsonData data = new JsonData();
		data["name"] = username;
		data["password"] = password1;
		String message = MessagePacker.pack (MessagePacker.Type.REGISTER, MessagePacker.TargetType.SYSTEM, data);
		ClientSocket.GetInstance ().SendMessage (message);
	}

	// Check password
	public void CheckPassword(){
		if (RegPasswordObj1.GetComponent<InputField>().text != RegPasswordObj2.GetComponent<InputField>().text) {
			PasswordTipText.text = "Passwords should be same!";
		} else {
			PasswordTipText.text = "";
		}
	}

	// Check result of login and register
	private void CheckResult(MessagePacker.Type type, MessagePacker.TargetType targetType){
		JsonData data = ClientSocket.GetInstance ().GetMessage (type, targetType);
		int i = 0;
		while (data == null && i<=5) {
			Thread.Sleep (1000);
			i++;
		}
		if (data == null) {
			MessageTip.SetTip (type+" time out!");  
		} else if((int)data["code"] == 1){
			if (type == MessagePacker.Type.REGISTER) {
				OnClickBack ();
				MessageTip.SetTip ("Register success, please login!");  
			} else {
				SceneManager.LoadScene ("Main");
			}
		}
	}

	// Clear tip
	private void ClearTips(){
		UsernameTipText.text = "";
		PasswordTipText.text = "";
	}

	// Clear register info
	private void ClearRegisterInfo(){
		RegUsernameText.text = "";
		RegPasswordObj1.GetComponent<InputField> ().text = "";
		RegPasswordObj2.GetComponent<InputField> ().text = "";
	}
}
