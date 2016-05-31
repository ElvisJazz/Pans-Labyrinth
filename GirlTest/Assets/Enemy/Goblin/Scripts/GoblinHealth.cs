//
// Control goblin health
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using System.Collections;

public class GoblinHealth : EnemyHealth {
	override protected void UpdateHealthDisplayRef(EnemyHealth health){
		healthInfoController._GoblinHealth = health as GoblinHealth;
	}
}
