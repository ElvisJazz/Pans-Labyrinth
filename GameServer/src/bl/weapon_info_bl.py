# ======================================================================
# Function: Business Logic of WeaponInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from bl.base_bl import BaseBL
from dao.weapon_info_dao import WeaponInfoDao


class WeaponInfoBL(BaseBL):

    def __init__(self, player_id):
        self.dao = WeaponInfoDao(player_id)

    # Get weapon list
    def get_list(self):
        return self.dao.get_list_by_player_id()

    # Add weapon list
    def add_list(self, weapon_info_list):
        for info in weapon_info_list:
            if self.dao.insert(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Update weapon record list
    def update_list(self, weapon_info_list):
        for info in weapon_info_list:
            if self.dao.update(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Update weapon record list
    def delete_list(self, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.delete(info.weapon_id) <= 0:
               return False
        #self.dao.commit()
        return True
