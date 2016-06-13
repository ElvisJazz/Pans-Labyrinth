using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour {
	// Client socket
	private ClientSocket socket = null;
	// Escape press
	bool isEscPress = false;
	// View controller
	public CameraController ViewController = null;

	// Use this for initialization
	void Start () {
		if (SceneManager.GetActiveScene ().name == "Main") {
			PlayerManager.Init ();
			Cursor.visible = false;
			Screen.fullScreen = true;
			socket = ClientSocket.GetInstance ();
		} else {
			Cursor.visible = true;
		}
	}
	
	// Update is called once per frame
	void Update () {
		if (socket != null)
			ReadServerMessage ();
		if (SceneManager.GetActiveScene ().name == "Main") {
			UpdateCursor ();
			CheckConnected ();
		} else {
			Cursor.visible = true;
		}

	}

	void OnApplicationQuit(){
		ClientSocket.GetInstance ().Close ();
	}

	// Check whether has server message to read
	void ReadServerMessage(){
		string message = socket.PopMessageList ();
		if (message != null) {
			Dispatcher.dispatcher (message);
		}
	}


	// Update visibility of curson
	void UpdateCursor(){
		if (Input.GetKeyDown (KeyCode.Escape)) {
			Cursor.visible = true;
			isEscPress = true;
			ViewController.SetCameraPositionNormalView ();
			MessageTip.SetOption ();
		} else if (!isEscPress && !WeaponInfoController.isContainerVisible && Cursor.visible) {
			Cursor.visible = false;
		} else if (isEscPress && Input.GetMouseButtonDown (0)) {
			Cursor.visible = false;
			isEscPress = false;
		}
	}

	// Check connection valid
	void CheckConnected(){
		if (!ClientSocket.GetInstance ().IsConnected ()) {
			SceneManager.LoadScene (0);
		}
	}
}
