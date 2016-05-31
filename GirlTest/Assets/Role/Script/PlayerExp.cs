using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class PlayerExp : MonoBehaviour {

	// Player's exp
	int exp = 0;
	public int Exp {
		get{
			return exp;
		}
	}
	// Max player's exp
	public int MaxExp = 1000;
	// Exp color
	public Color ExpColor = Color.blue; 

	// Use this for initialization
	void Start () {
		// Init gameController
		//		GameObject gameControllerObject = GameObject.FindWithTag ("GameController");
		//		if (gameControllerObject != null) {
		//			gameController = gameControllerObject.GetComponent<GameController> ();
		//		}else {
		//			Debug.Log("Cannot find GameControll script");
		//		}
		//Init info controller
		GameObject InfoManager = GameObject.Find("InfoManager");
		if (InfoManager != null) {
			InfoManager.GetComponent<ExpInfoController> ()._PlayerExp = this;
		}
	}

	// Get hurt
	public void AddExp(int amount){
		exp += amount;
		if (exp > MaxExp) {
			Promote ();
		} 
	}

	// Add level
	void Promote(){
		//gameController.GameOver ();
	}

}
