# ======================================================================
# Function: Business Logic of EnemyConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from bl.base_bl import BaseBL
from dao.enemy_config_info_dao import EnemyConfigInfoDao


class EnemyConfigInfoBL(BaseBL):

    def __init__(self, player_id):
        self.dao = EnemyConfigInfoDao(player_id)

    # Get enemy config list
    def get_list(self):
        return self.dao.get_enemy_config_list()