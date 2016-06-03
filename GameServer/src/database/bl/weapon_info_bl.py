# ======================================================================
# Function: Business Logic of WeaponInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.weapon_info_dao import WeaponInfoDao


class WeaponInfoBL(BaseBL):

    def __init__(self, player_id, conn=None, has_own_conn=False):
        self.dao = WeaponInfoDao(player_id, conn, has_own_conn)

    # Get weapon dict
    def get_dict(self):
        return self.dao.get_dict_by_player_id()

    # Add weapon list
    def add_list(self, weapon_info_list):
        for info in weapon_info_list:
            if self.dao.insert(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Update weapon record dict
    def update_dict(self, weapon_info_dict):
        for info in weapon_info_dict.values():
            if self.dao.update(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Update weapon record list
    def delete_dict(self, enemy_info_dict):
        for info in enemy_info_dict.values():
            if self.dao.delete(info.weapon_id) <= 0:
               return False
        #self.dao.commit()
        return True
