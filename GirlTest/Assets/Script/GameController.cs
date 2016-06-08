using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

[System.Serializable]
public class q{
	public int qq;
	public q(int qqq){
		qq = qqq;
	}
}

[System.Serializable]
public class p{
	public int a;
	public q[,] pp;
}

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
		
//		p pp = new p ();
//		pp.a = 2;
//		pp.pp = new q[2,2];
//		pp.pp [0,0] = new q(3);
//		pp.pp [0,1] = new q(3);
//		pp.pp [1,0] = new q(4);
//		pp.pp [1,1] = new q(4);
//		string s = JsonUtility.ToJson (pp);
//		p ppp = JsonUtility.FromJson<p> (s);
//		Debug.Log (1);
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
