using System;
using UnityEngine;


public class MessageTip : MonoBehaviour
{
	// Tip
	private static string tip = "The connection is aborted!";
	// Is show
	private static bool isShow = false;

	void OnGUI(){
		if (isShow) {
			GUI.Box (new Rect (Screen.width / 2 - 100, Screen.height / 4, 280, 140), "");
			GUI.Label(new Rect(Screen.width / 2 - 80, Screen.height / 4 + 20, 240, 80), tip);
			if (GUI.Button (new Rect (Screen.width / 2 + 20, Screen.height / 4 + 100, 40, 20), "OK")) {
				isShow = false;
			}
		}
	}

	public static void SetTip(string message){
		tip = message;
		isShow = true;
	}
}

