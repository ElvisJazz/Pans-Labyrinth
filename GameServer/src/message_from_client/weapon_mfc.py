# ======================================================================
# Function: Message of the weapon which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.weapon_info import WeaponInfo


class WeaponMessageFromClient(object):

    def get_weapon_id(self):
        if hasattr(self, 'weapon_id'):
            return self.weapon_id
        else:
            return -1

    def set_weapon_info(self, weapon_info):
        if isinstance(weapon_info, WeaponInfo):
            if hasattr(self, 'weapon_id'):
                weapon_info.weapon_id = self.weapon_id
            if hasattr(self, 'take'):
                weapon_info.take = self.take
            if hasattr(self, 'current_bullets_in_gun'):
                weapon_info.current_bullets_in_gun = self.current_bullets_in_gun
            if hasattr(self, 'current_bullets_in_bag'):
                weapon_info.current_bullets_in_bag = self.current_bullets_in_bag
        else:
            raise Exception("Instance of WeaponInfo is expected!")

    def set_weapon_list(self, weapon_dict):
        if isinstance(weapon_dict, dict):
            if hasattr(self, 'weapon_info_list'):
                weapon_info_list = self.weapon_info_list
                for weapon_info in weapon_info_list:
                    weapon = weapon_dict[weapon_info["weapon_id"]]
                    if weapon_info.has_key('take'):
                        weapon.take = weapon_info["take"]
                    if weapon_info.has_key('current_bullets_in_gun'):
                        weapon.current_bullets_in_gun = weapon_info["current_bullets_in_gun"]
                    if weapon_info.has_key('current_bullets_in_bag'):
                        weapon.current_bullets_in_bag = weapon_info["current_bullets_in_bag"]
            else:
                raise Exception("Instance of List for weapon is expected!")
        else:
            raise Exception("Instance of Dict for weapon is expected!")