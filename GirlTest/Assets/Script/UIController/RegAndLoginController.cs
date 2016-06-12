using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System;
using System.Threading;
using UnityEngine.SceneManagement;

public class RegAndLoginController : MonoBehaviour {

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
		SystemManager.SendRegiserAndLoginMessage(MessageConstant.Type.LOGIN, username, password);
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
		if (SystemManager.SendRegiserAndLoginMessage (MessageConstant.Type.REGISTER, username, password1))
			OnClickBack ();
	}

	// Check password
	public void CheckPassword(){
		if (RegPasswordObj1.GetComponent<InputField>().text != RegPasswordObj2.GetComponent<InputField>().text) {
			PasswordTipText.text = "Passwords should be same!";
		} else {
			PasswordTipText.text = "";
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
