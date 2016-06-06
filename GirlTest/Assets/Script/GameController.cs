using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;
using LitJson;

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
		//JsonData data = JsonMapper.ToObject ("{\"1\" : [0,1,2]}");
		//Debug.Log(data["1"]);

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
		JsonData data = socket.PopMessageList ();
		if (data != null) {
			Dispatcher.dispatcher (data);
		}
	}

}
