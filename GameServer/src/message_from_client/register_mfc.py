# ======================================================================
# Function: Message of the weapon which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from src.info.weapon_info import WeaponInfo


class RegisterMessageFromClient(object):

    def __init__(self):
        pass;

    def set_enemy_info(self, weapon_info):
        if isinstance(weapon_info, WeaponInfo):
            if hasattr(self, '_weapon_id'):
                weapon_info._weapon_id = self._weapon_id
            elif hasattr(self, '_fetch'):
                weapon_info._health = self._fetch
        else:
            raise Exception("Instance of WeaponInfo is expected!")