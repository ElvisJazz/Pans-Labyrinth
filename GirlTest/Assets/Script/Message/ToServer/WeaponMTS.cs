using System;
using System.Collections.Generic;

[System.Serializable]
public class WeaponMessageToServer : BaseMessage {
	// Weapon id
	public int weapon_id;
	// Whether be taken
	public int take;
	// Current bullets in gun
	public int current_bullets_in_gun;
	// Current bullets in bag
	public int current_bullets_in_bag;

	public WeaponMessageToServer(int message_type, int target_type, int weapon_id, int take, int current_bullets_in_gun, int current_bullets_in_bag):base(message_type, target_type){
		this.weapon_id = weapon_id;
		this.take = take;
		this.current_bullets_in_gun = current_bullets_in_gun;
		this.current_bullets_in_bag = current_bullets_in_bag;
	}
}

[System.Serializable]
public class WeaponMessage {
	// Weapon id
	public int weapon_id;
	// Whether be taken
	public int take;
	// Current bullets in gun
	public int current_bullets_in_gun;
	// Current bullets in bag
	public int current_bullets_in_bag;

	public WeaponMessage(int weapon_id, int take, int current_bullets_in_gun, int current_bullets_in_bag){
		this.weapon_id = weapon_id;
		this.take = take;
		this.current_bullets_in_gun = current_bullets_in_gun;
		this.current_bullets_in_bag = current_bullets_in_bag;
	}
}

[System.Serializable]
public class WeaponListMessageToServer : BaseMessage {
	public List<WeaponMessage> weapon_info_list = new List<WeaponMessage>();

	public WeaponListMessageToServer(int message_type, int target_type) : base(message_type, target_type){

	}
}
