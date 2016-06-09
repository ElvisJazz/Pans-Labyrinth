using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class PlayerHealth : MonoBehaviour {

	// Player's health
	int health = 100;
	public int Health {
		get{
			return health;
		}
		set{
			health = value; 
		}
	}
	// Damage image
	public Image DamageImage = null;
	// Damge color
	public Color DamageColor;
	// Flash speed
	public float FlashSpeed = 5.0f;
	// Max player's health
	public int MaxHealth = 100;
	// Health color
	public Color HealthColor = Color.green; 
	// Game controller
	//GameController gameController;
	// Animator
	Animator playerAnimator;
	// Health information controller
	HealthInfoController healthInfoController = null;
	// Get hurt
	bool isDamage = false;
	// Is dead
	public bool IsDead = false;
	// Animator state
	static int damageState = Animator.StringToHash("Base Layer.Damaged");


	// Use this for initialization
	void Start () {
		health = MaxHealth;
		// Get animator
		playerAnimator = GetComponent<Animator>();
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
			healthInfoController = InfoManager.GetComponent<HealthInfoController> ();
			healthInfoController._PlayerHealth = this;
		}
	}

	// Update
	void Update(){
		UpdateDamageEffect ();
	}

	// Get hurt
	public void GetHurt(int amount){
		health -= amount;
		isDamage = true;
		if (health <= 0) {
			health = 0;
			Death ();
		} else if(playerAnimator.GetCurrentAnimatorStateInfo (0).fullPathHash != damageState && !playerAnimator.IsInTransition(0)){
			playerAnimator.SetTrigger ("Damage");
		}

		UpdateHealthColor ();
	}

	// Add health value
	public void AddHealthValue(int value){
		health += value;
		if (health > MaxHealth) {
			health = MaxHealth;
		}

		UpdateHealthColor ();
	}

	// Death
	void Death(){
		playerAnimator.SetTrigger ("Die");
		IsDead = true;
		//gameController.GameOver ();
	}
		
	// Set health color
	void UpdateHealthColor(){
		float rate = (float)health / MaxHealth;
		if (rate <= 0.33f) {
			HealthColor = Color.red;
		} else if (rate <= 0.66f) {
			HealthColor = Color.yellow;
		} else {
			HealthColor = Color.green;
		}
	}

	// Update damage effect
	void UpdateDamageEffect(){
		if (isDamage) {
			DamageImage.color = DamageColor;
			isDamage = false;
		} else {
			DamageImage.color = Color.Lerp (DamageImage.color, Color.clear, FlashSpeed * Time.deltaTime);
		}
	}

}
