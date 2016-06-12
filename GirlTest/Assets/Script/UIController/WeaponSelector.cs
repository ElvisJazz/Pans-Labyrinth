using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using System.Collections;

public class WeaponSelector : Selectable {
	// Weapon info controller script
	WeaponInfoController weaponInfoController;
	// Original normal color
	Color originalNormalColor;
	// Weapon img container
	GameObject container;

	// Start
	new void Start(){
		originalNormalColor = base.colors.normalColor;
		// Set weapon img container
		container = GameObject.Find("WeaponContainer");
		GameObject weaponInfo = GameObject.Find ("InfoManager");
		if (weaponInfo != null) {
			weaponInfoController = weaponInfo.GetComponent<WeaponInfoController> ();
		}
		base.Start ();
	}

	// Select
	override public void OnSelect(BaseEventData evenData){
		int index = gameObject.name.LastIndexOf ("(Clone)");
		if (index != -1) {
			gameObject.name = gameObject.name.Substring (0, index);
		}
		weaponInfoController.SelectNewWeapon (gameObject.name);
		base.OnSelect (evenData);
		SetOtherUnselected ();
		SetSelectedState (true);
	}

	// Set others unselected
	void SetOtherUnselected(){
		foreach(Transform child in container.transform){
			child.gameObject.GetComponent<WeaponSelector> ().SetSelectedState (false);
		}
	}

	// Set selected state
	public void SetSelectedState(bool selected){
		ColorBlock colorBlock = new ColorBlock ();
		colorBlock = base.colors;
		if (selected) {
			colorBlock.normalColor = colorBlock.highlightedColor;
		} else {
			colorBlock.normalColor = originalNormalColor;
		}
		base.colors = colorBlock;
	}
}
