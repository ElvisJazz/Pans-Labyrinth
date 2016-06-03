# ======================================================================
# Function: Manage information of the enemy
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from database.bl.enemy_info_bl import EnemyInfoBL
from message_from_client.enemy_mfc import EnemyMessageFromClient


class EnemyManager(object):
    def __init__(self, player_id):
        self._player_id = player_id
        self._alive_enemy_dict = {}
        self._dead_enemy_list = []

    def save(self):
        """save the information of enemy"""
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        flag = enemy_info_bl.update_dict(self._alive_enemy_dict)
        flag |= enemy_info_bl.delete_list(self._dead_enemy_list)
        return flag

    def load(self):
        """load the information of enemy"""
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        self._alive_enemy_dict = enemy_info_bl.get_dict()

    def update(self, enemy_mfc):
        """ update enemy info """
        if isinstance(enemy_mfc, EnemyMessageFromClient):
            id = enemy_mfc.get_enemy_id()
            if id != -1:
                enemy_mfc.set_enemy_info(self._alive_enemy_dict[id])
                # if enemy is dead, pop it from dead dict to living list
                if self._alive_enemy_dict[id].health <= 0:
                    self._dead_enemy_list.append(self._alive_enemy_dict.pop(id))