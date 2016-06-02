# ======================================================================
# Function: Business Logic of PlayerInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from bl.base_bl import BaseBL
from dao.player_info_dao import PlayerInfoDao


class PlayerInfoBL(BaseBL):

    def __init__(self, player_id):
        self.dao = PlayerInfoDao(player_id)

    # Get player info
    def get_by_id(self):
        return self.dao.get_by_id()

    # Add player
    def add_player(self, player_info):
        rc = self.dao.insert(player_info)
        #self.dao.commit()
        return rc > 0

    # Update player
    def update_player(self, player_info):
        rc = self.dao.update(player_info)
        #self.dao.commit()
        return rc > 0

    # Update player
    def delete_list(self, player_info):
        rc = self.dao.delete(player_info)
        #self.dao.commit()
        return rc > 0
