# ======================================================================
# Function: Business Logic of EnemyInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.enemy_info_dao import EnemyInfoDao


class EnemyInfoBL(BaseBL):

    def __init__(self, player_id, conn=None, has_own_conn=False):
        self.dao = EnemyInfoDao(player_id, conn, has_own_conn)

    # Get enemy dict
    def get_dict(self):
        return self.dao.get_dict_by_player_id()

    # Add enemy list
    def add_list(self, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.insert(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Update enemy record dict
    def update_dict(self, enemy_info_dict):
        for info in enemy_info_dict.values():
            if self.dao.update(info) <= 0:
               return False
        #self.dao.commit()
        return True

    # Delete enemy record list
    def delete_list(self, enemy_info_dict):
        for info in enemy_info_dict.values():
            if self.dao.delete(info.enemy_id) <= 0:
               return False
        #self.dao.commit()
        return True
