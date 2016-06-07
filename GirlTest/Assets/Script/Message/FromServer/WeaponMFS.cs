using System;

[System.Serializable]
public class WeaponMessageFromServer : BaseMessage {
	// Type id
	public int type_id;
	// Position
	public float[] position;
	// Whether be taken
	public int take;
	// Name
	public string name;
	// Current bullets in gun
	public int current_bullets_in_gun;
	// Current bullets in bag
	public int current_bullets_in_bag;
	// Max Current bullets in gun
	public int max_current_bullets_in_gun;
	// Max current bullets in bag
	public int max_current_bullets_in_bag;
}
