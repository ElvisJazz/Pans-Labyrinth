using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour {
	// Client socket
	private ClientSocket socket = null;

	// Use this for initialization
	void Start () {
		if (SceneManager.GetActiveScene ().name == "Main") {
			Cursor.visible = false;
			Screen.fullScreen = true;
			socket = ClientSocket.GetInstance ();
		}
	}
	
	// Update is called once per frame
	void Update () {
		if(socket != null)
			ReadServerMessage ();
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

}
