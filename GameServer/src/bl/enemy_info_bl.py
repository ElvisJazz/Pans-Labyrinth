# ======================================================================
# Function: Business Logic of EnemyInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.dao.enemy_info_dao import EnemyInfoDao


class EnemyInfoBL(object):

    def __init__(self):
        self.dao = EnemyInfoDao()

    # Get enemy list
    def get_list(self, player_id):
        return self.dao.get_list_by_player_id(player_id)

    # Add enemy list
    def add_list(self, player_id, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.insert(player_id, info) <= 0:
               return False
        self.dao.commit()
        return True

    # Update enemy record list
    def update_list(self, player_id, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.update(player_id, info) <= 0:
               return False
        self.dao.commit()
        return True

    # Update enemy record list
    def delete_list(self, player_id, enemy_info_list):
        for info in enemy_info_list:
            if self.dao.delete(player_id, info) <= 0:
               return False
        self.dao.commit()
        return True
