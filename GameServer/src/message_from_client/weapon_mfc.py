# ======================================================================
# Function: Message of the weapon which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.weapon_info import WeaponInfo


class WeaponMessageFromClient(object):

    def __init__(self):
        pass;

    def set_enemy_info(self, weapon_info):
        if isinstance(weapon_info, WeaponInfo):
            if hasattr(self, 'weapon_id'):
                weapon_info.weapon_id = self.weapon_id
            if hasattr(self, 'fetch'):
                weapon_info.health = self.fetch
        else:
            raise Exception("Instance of WeaponInfo is expected!")