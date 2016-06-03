# ======================================================================
# Function: Business Logic of PlayerConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.player_config_info_dao import PlayerConfigInfoDao


class PlayerConfigInfoBL(BaseBL):

    def __init__(self, player_id, conn=None, has_own_conn=False):
        self.dao = PlayerConfigInfoDao(player_id, conn, has_own_conn)

    # Get player config
    def get_by_id(self, id):
        return self.dao.get_player_config_by_id(id)