# ======================================================================
# Function: Business Logic of PlayerConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from bl.base_bl import BaseBL
from dao.player_config_info_dao import PlayerConfigInfoDao


class PlayerConfigInfoBL(BaseBL):

    def __init__(self, player_id):
        self.dao = PlayerConfigInfoDao(player_id)

    # Get player config
    def get_by_id(self, id):
        return self.dao.get_player_config_by_id(id)