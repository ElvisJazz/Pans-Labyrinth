using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour {

	// Use this for initialization
	void Start () {
		if (SceneManager.GetActiveScene ().name == "Main") {
			Cursor.visible = false;
			Screen.fullScreen = true;
		}
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	void OnApplicationQuit(){
		ClientSocket.GetInstance ().Close ();
	}

}
