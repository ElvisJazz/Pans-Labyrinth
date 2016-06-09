//
// Control enemy state as base class
// 
// 2016/05/17 Elvis Jia
//
using UnityEngine;
using System.Collections;

public class EnemyState : MonoBehaviour {

	// Is active
	bool isActive = false;
	public bool Active{
		get{
			return isActive;
		}
		set{
			isActive = value;
		}
	}
	// Is attack
	bool isAttack = false;
	public bool Attack{
		get{
			return isAttack;
		}
		set{
			isAttack = value;
		}
	}
	// Is run
	bool isRun = false;
	public bool Run{
		get{
			return isRun;
		}
		set{
			isRun = value;
		}
	}
}
