//
// Control monster health
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using System.Collections;

public class MonsterHealth : EnemyHealth {

	// Blood block
	public GameObject BloodBlock;
	// Bullets supply
	public GameObject BulletsSupply;
	// Amount of blood blocks when monster dies
	public int Amount = 3;
	// Power of bounce 
	public float power = 6f;
	// Pos of blood block spawner
	public Transform BloodSpawner;
	// Bullets supply spawner
	public Transform SupplySpawner;

	new void Start(){
		base.Start ();
		UpdateHealthDisplayRef (this);
	}

	override protected void UpdateHealthDisplayRef(EnemyHealth health){
		healthInfoController._MonsterHealth = health as MonsterHealth;
	}

	// Drop something
	override protected void DropSomething(){
		for (int i = 0; i < Amount; i++) {
			GameObject blood = Instantiate (BloodBlock, BloodSpawner.position, BloodSpawner.rotation) as GameObject;
			Random.seed = (int)Time.deltaTime * 100;
			Vector2 vec = Random.insideUnitCircle * power;
			blood.GetComponent<Rigidbody> ().AddForce (new Vector3(vec.x, power, vec.y), ForceMode.VelocityChange);
		}

		Instantiate (BulletsSupply, SupplySpawner.position, Quaternion.identity);
	}
}
