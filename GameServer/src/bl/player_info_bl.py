# ======================================================================
# Function: Business Logic of PlayerInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.dao.player_info_dao import PlayerInfoDao


class PlayerInfoBL(object):

    def __init__(self):
        self.dao = PlayerInfoDao()

    # Get player info
    def get_by_id(self, player_id):
        return self.dao.get_by_id(player_id)

    # Add player
    def add_player(self, player_info):
        rc = self.dao.insert(player_info)
        self.dao.commit()
        return rc > 0

    # Update player
    def update_player(self, player_info):
        rc = self.dao.update(player_info)
        self.dao.commit()
        return rc > 0

    # Update player
    def delete_list(self, player_info):
        rc = self.dao.delete(player_info)
        self.dao.commit()
        return rc > 0