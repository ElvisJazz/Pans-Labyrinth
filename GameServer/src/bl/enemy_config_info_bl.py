# ======================================================================
# Function: Business Logic of EnemyConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from src.dao.enemy_config_info_dao import EnemyConfigInfoDao


class EnemyInfoBL(object):

    def __init__(self):
        self.dao = EnemyConfigInfoDao()

    # Get enemy config list
    def get_list(self):
        return self.dao.get_enemy_config_list()