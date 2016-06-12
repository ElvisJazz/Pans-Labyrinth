using System;
using UnityEngine;
using UnityEngine.SceneManagement;


public class MessageTip : MonoBehaviour
{
	// Tip
	private static string tip = "The connection is aborted!";
	// Is show tip
	private static bool isShowTip = false;
	// Is show option
	private static bool isShowOp = false;
	// Is relogin
	private static bool isRelogin = false;

	void OnGUI(){
		if (isShowTip || isShowOp) {
			Cursor.visible = true;
			GUI.Box (new Rect (Screen.width / 2 - 100, Screen.height / 4, 280, 140), "");
			GUI.Label (new Rect (Screen.width / 2 - 80, Screen.height / 4 + 20, 240, 80), tip);
			if (isShowTip) {
				if (GUI.Button (new Rect (Screen.width / 2 + 20, Screen.height / 4 + 100, 40, 20), "OK")) {
					isShowTip = false;
					Cursor.visible = false;
					if (isRelogin) {
						SceneManager.LoadScene (0);
						isRelogin = false;
					}
				}
			} else {
				Time.timeScale = 0;
				if (GUI.Button (new Rect (Screen.width / 2 -75, Screen.height / 4 + 100, 65, 20), "SAVE")) {
					isShowOp = false;
					SystemManager.Save ();
					Time.timeScale = 1;
				}
				if (GUI.Button (new Rect (Screen.width / 2 , Screen.height / 4 + 100, 65, 20), "EXIT")) {
					Application.Quit ();
				}
				if (GUI.Button (new Rect (Screen.width / 2 + 75, Screen.height / 4 + 100, 65, 20), "CANCLE")) {
					isShowOp = false;
					Time.timeScale = 1;
				}
			}

		}
	}

	public static void SetTip(string message, bool isRelogin=false){
		tip = message;
		isShowTip = true;
		isShowOp = false;
		isRelogin = isRelogin;
	}

	public static void SetOption(){
		tip = "是否保存当前进度信息，直接退出将失去包括当前等级、经验、体力等所有信息，下次登陆将回到上次存盘点！";
		isShowOp = true;
		isShowTip = false;
	}
}

