# ======================================================================
# Function: Business Logic of PlayerConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from src.dao.player_config_info_dao import PlayerConfigInfoDao


class PlayerInfoBL(object):

    def __init__(self):
        self.dao = PlayerConfigInfoDao()

    # Get player config
    def get_by_id(self, id):
        return self.dao.get_player_config_by_id(id)