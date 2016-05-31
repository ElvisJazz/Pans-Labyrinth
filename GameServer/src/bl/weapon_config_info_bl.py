# ======================================================================
# Function: Business Logic of WeaponConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from src.dao.weapon_config_info_dao import WeaponConfigInfoDao


class WeaponConfigInfoBL(object):

    def __init__(self, player_id):
        self.dao = WeaponConfigInfoDao(player_id)

    # Get enemy config list
    def get_list(self):
        return self.dao.get_weapon_config_list()