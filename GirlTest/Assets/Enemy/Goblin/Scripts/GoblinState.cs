//
// Control goblin state
// 
// 2016/05/06 Elvis Jia
//
using UnityEngine;
using System.Collections;

public class GoblinState : EnemyState {

	// Store reference and material of components of all sub-gameobjects which can become a stone and has mesh render or skinned mesh render
	Hashtable stoneComponentTable;
	// Stone Material
	public Material StoneMaterial;

	void Start(){
		Active = true;
		GetComponent<Animator>().SetTrigger("Idle");
	}

	// Use this for initialization
	void Awake () {
		stoneComponentTable = new Hashtable ();
		GameObject[] gameObjects = GameObject.FindGameObjectsWithTag ("StoneMesh");
		foreach (GameObject gameObject in gameObjects) {
			// Find the component which has set materials
			Renderer component = gameObject.GetComponent<SkinnedMeshRenderer>();
			if (component == null) {
				component = gameObject.GetComponent<MeshRenderer> ();
			}
			if (component != null) {
				stoneComponentTable.Add(component, component.material);
			}
		}
	}
	
	// Update is called once per frame
	void Update () {
	}

	// Make Gobin seem like a stone
	public void MakeLikeStone(){
		foreach (Renderer component in stoneComponentTable.Keys) {
			if(component != null)
				component.material = StoneMaterial;
		}	
		Active = false;
	}

	// Active Gobin which used to seem like a stone
	public void ActiveGoblin(){
		foreach (Renderer component in stoneComponentTable.Keys) {
			component.material = stoneComponentTable[component] as Material;
		}
		Active = true;
		GetComponent<Animator>().SetTrigger("Idle");
	}

}
