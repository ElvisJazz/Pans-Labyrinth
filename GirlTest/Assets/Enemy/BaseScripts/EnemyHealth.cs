//
// Control enemy health as base class
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class EnemyHealth : MonoBehaviour {
	// Max Health
	public int MaxHealth = 100;
	// Health
	int health;
	public int Health {
		get{
			return health;
		}
	}
	// Health color
	public Color healthColor = Color.green; 
	// Game controller
	//GameController gameController;
	// Award exp of death
	public int exp = 20;
	// Is dead
	bool isDead = false;
	// Animator
	Animator enemyAnimator;
	// Health information controller
	protected HealthInfoController healthInfoController = null;
	// Exp script of the player
	PlayerExp playerExp = null;
	// Is sinking
	bool isSinking = false;
	// Sink speed
	public float SinkSpeed = 2.5f;
	// Animator state
	static int damageState = Animator.StringToHash("Base Layer.Block_hit");

	// Use this for initialization
	protected void Start () {
		health = MaxHealth;
		// Get animator
		enemyAnimator = GetComponent<Animator>();
		// Init gameController
//		GameObject gameControllerObject = GameObject.FindWithTag ("GameController");
//		if (gameControllerObject != null) {
//			gameController = gameControllerObject.GetComponent<GameController> ();
//		}
		//Init info controller
		GameObject InfoManager = GameObject.Find("InfoManager");
		if (InfoManager != null) {
			healthInfoController = InfoManager.GetComponent<HealthInfoController> ();
		}
		//Init player exp controller
		GameObject player = GameObject.Find("Player");
		if (player != null) {
			playerExp = player.GetComponent<PlayerExp> ();
		}
	}

	// Update
	void Update(){
		if(isSinking)
		{
			transform.Translate (-Vector3.up * SinkSpeed * Time.deltaTime);
		}
	}

	// Get hurt
	public void GetHurt(int amount){
		if (!isDead) {
			health -= amount;
			UpdateHealthColor ();
			if (health <= 0) {
				health = 0;
				Die ();
				UpdateHealthDisplayRef (null);
			} else if (enemyAnimator.GetCurrentAnimatorStateInfo (0).fullPathHash != damageState && !enemyAnimator.IsInTransition (0)) {
				enemyAnimator.SetTrigger ("Damage");
				UpdateHealthDisplayRef (this);
			}
		}
	}

	// Die
	void Die(){
		playerExp.AddExp (exp);
		isDead = true;
		enemyAnimator.SetTrigger ("Die");
	}

	// Update enemy health reference of info controller 
	virtual protected void UpdateHealthDisplayRef(EnemyHealth health){
	}

	// Set health color
	void UpdateHealthColor(){
		float rate = (float)health / MaxHealth;
		if (rate <= 0.33f) {
			healthColor = Color.red;
		} else if (rate <= 0.66f) {
			healthColor = Color.yellow;
		} else {
			healthColor = Color.green;
		}
	}

	// Start sinking
	public void StartSinking(){
		isSinking = true;
		Destroy (gameObject, 2f);
	}

	// After dead
	public void AfterDead(){
		// Drop something
		DropSomething();
		StartSinking ();
	}

	// Drop something
	virtual protected void DropSomething(){
	}
}
