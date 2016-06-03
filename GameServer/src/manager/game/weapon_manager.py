# ======================================================================
# Function: Manage information of the weapon
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from database.bl.weapon_info_bl import WeaponInfoBL
from message_from_client.weapon_mfc import WeaponMessageFromClient


class WeaponManager(object):
    def __init__(self, player_id):
        self._player_id = player_id
        self._weapon_dict = {}

    def save(self):
        """save the information of weapon"""
        weapon_info_bl = WeaponInfoBL(self._player_id, None, True)
        flag = weapon_info_bl.update_dict(self._weapon_dict)
        return flag

    def load(self):
        """load the information of weapon"""
        weapon_info_bl = WeaponInfoBL(self._player_id, None, True)
        self._weapon_dict = weapon_info_bl.get_dict()

    def update(self, weapon_mfc):
        """ update enemy info """
        if isinstance(weapon_mfc, WeaponMessageFromClient):
            id = weapon_mfc.get_weapon_id()
            if id != -1:
                weapon_mfc.set_weapon_info(self._weapon_dict[id])