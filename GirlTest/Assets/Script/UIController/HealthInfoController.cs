//
// Control health info
// 
// 2016/05/18 Elvis Jia
//
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class HealthInfoController : MonoBehaviour {
	// Goblin health slider block
	public GameObject GoblinSlider = null;
	// Monster health slider block
	public GameObject MonsterSlider = null;
	// Player health slider block
	public GameObject PlayerSlider = null;
	// Health slider of goblin, monster and player
	Slider goblinHealthSlider;
	Slider monsterHealthSlider;
	Slider playerHealthSlider;
	// Goblin and monster health fill
	public Image GoblinHealthFill;
	public Image MonsterHealthFill;
	public Image PlayerHealthFill;
	// Player health text
	public Text PlayerHealthText = null;
	// Goblin slider position
	Vector3 goblinSliderPosition;
	// Monster slider position
	Vector3 monsterSliderPosition;
	// Refence of health of the goblin and the monster
	GoblinHealth goblinHealth = null;
	MonsterHealth monsterHealth = null;
	PlayerHealth playerHealth = null;
	public GoblinHealth _GoblinHealth {
		get {
			return goblinHealth;
		}
		set {
			goblinHealth = value;
		}
	}
	public MonsterHealth _MonsterHealth {
		get {
			return monsterHealth;
		}
		set {
			monsterHealth = value;
		}
	}
	public PlayerHealth _PlayerHealth {
		get {
			return playerHealth;
		}
		set {
			playerHealth = value;
		}
	}
	// Use this for initialization
	void Start () {
		// Set slider invisble
		GoblinSlider.SetActive(false);
		MonsterSlider.SetActive(false);
		// Get slider position
		goblinSliderPosition = GoblinSlider.transform.position;
		monsterSliderPosition = MonsterSlider.transform.position;
		// Get slider refence
		goblinHealthSlider = GoblinSlider.GetComponentInChildren<Slider>();
		monsterHealthSlider = MonsterSlider.GetComponentInChildren<Slider> ();
		playerHealthSlider = PlayerSlider.GetComponentInChildren<Slider> ();
	}
	
	// Update is called once per frame
	void Update () {
		UpdateHealthSlider ();
		SetHealthVisible ();
		DisplayHealth ();
		UpdateHealthText ();
	}

	// Update slider position
	public void UpdateHealthSlider(){
		if (monsterHealth != null) {
			MonsterSlider.transform.position = monsterSliderPosition;
			if (goblinHealth != null) {
				GoblinSlider.transform.position = goblinSliderPosition;
			}
		} else {
			if (goblinHealth != null) {
				GoblinSlider.transform.position = monsterSliderPosition;
			}
		}
	}

	// Set health slider visible
	void SetHealthVisible(){
		GoblinSlider.SetActive (goblinHealth!=null? true: false);
		MonsterSlider.SetActive (monsterHealth!=null? true: false);
	}

	// Display enemy health
	public void DisplayHealth(){
		if (monsterHealth != null) {
			monsterHealthSlider.value = monsterHealth.Health;
			MonsterHealthFill.color = monsterHealth.healthColor;
		}
		if (goblinHealth != null) {
			goblinHealthSlider.value = goblinHealth.Health;
			GoblinHealthFill.color = goblinHealth.healthColor;
		}
		if (playerHealth != null) {
			playerHealthSlider.value = playerHealth.Health;
			PlayerHealthFill.color = playerHealth.HealthColor;
		}
	}

	// Update health text
	void UpdateHealthText(){
		if (playerHealth != null) {
			PlayerHealthText.text = playerHealth.Health + "/" + playerHealth.MaxHealth;
		}
	}
}
