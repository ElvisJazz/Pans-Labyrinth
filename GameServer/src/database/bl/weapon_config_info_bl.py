# ======================================================================
# Function: Business Logic of WeaponConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.weapon_config_info_dao import WeaponConfigInfoDao


class WeaponConfigInfoBL(BaseBL):

    def __init__(self, player_id, conn=None, has_own_conn=False):
        self.dao = WeaponConfigInfoDao(player_id, conn, has_own_conn)

    # Get enemy config list
    def get_list(self):
        return self.dao.get_weapon_config_list()