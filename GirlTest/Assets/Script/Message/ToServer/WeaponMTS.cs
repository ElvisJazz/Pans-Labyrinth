using System;

[System.Serializable]
public class WeaponMessageToServer : BaseMessage {
	// Weapon id
	public int weapon_id;
	// Whether be taken
	public int take;
}
