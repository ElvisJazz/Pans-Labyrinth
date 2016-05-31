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
}
