# ======================================================================
# Function: Business Logic of EnemyConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.enemy_config_info_dao import EnemyConfigInfoDao


class EnemyConfigInfoBL(BaseBL):

    def __init__(self, player_id, conn=None, has_own_conn=False):
        self.dao = EnemyConfigInfoDao(player_id, conn, has_own_conn)

    # Get enemy config list
    def get_list(self):
        return self.dao.get_enemy_config_list()