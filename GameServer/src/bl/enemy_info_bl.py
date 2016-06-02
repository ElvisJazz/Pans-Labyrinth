# ======================================================================
# Function: Business Logic of EnemyInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from bl.base_bl import BaseBL
from dao.enemy_info_dao import EnemyInfoDao


class EnemyInfoBL(BaseBL):

    def __init__(self, player_id):
        self.dao = EnemyInfoDao(player_id)

    # Get enemy list
    def get_list(self):
        return self.dao.get_list_by_player_id()

    # Add enemy list
    def add_list(self, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.insert(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Update enemy record list
    def update_list(self, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.update(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Delete enemy record list
    def delete_list(self, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.delete(info.enemy_id) <= 0:
               return False
        #self.dao.commit()
        return True
