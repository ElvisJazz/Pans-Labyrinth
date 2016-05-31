//
// Control exp info
// 
// 2016/05/18 Elvis Jia
//
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class ExpInfoController : MonoBehaviour {
	// Exp text
	public Text ExpText = null;
	// Exp slider of player
	public Slider PlayerExpSlider;
	// Exp fill of player
	public Image PlayerExpFill;
	// Player exp scirpt
	PlayerExp playerExp;
	public PlayerExp _PlayerExp {
		get {
			return playerExp;
		}
		set {
			playerExp = value;
		}
	}

	// Update is called once per frame
	void Update () {
		DisplayExp ();
		UpdateExpText ();
	}

	// Display exp
	public void DisplayExp(){
		if (playerExp != null) {
			PlayerExpSlider.value = playerExp.Exp;
			PlayerExpFill.color = playerExp.ExpColor;
		}
	}

	// Update exp text
	void UpdateExpText(){
		if (playerExp != null) {
			ExpText.text = playerExp.Exp + "/" + playerExp.MaxExp;
		}
	}
}
