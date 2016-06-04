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
        else:
            raise Exception("Instance of WeaponInfo is expected!")