# ======================================================================
# Function: Manage information of the player online
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from database.bl.player_info_bl import PlayerInfoBL
from info.player_info import PlayerInfo
from message_from_client.player_mfc import PlayerMessageFromClient


class PlayerManager(object):
    def __init__(self, player_id):
        self._player_id = player_id
        self._player_info = None

    def save(self):
        """save the information of player"""
        player_info_bl = PlayerInfoBL(self._player_id, None, True)
        flag = player_info_bl.update_player(self._player_info)
        return flag

    def load(self):
        """load the information of player"""
        player_info_bl = PlayerInfoBL(self._player_id, None, True)
        self._player_info = player_info_bl.get_by_id()

    def update(self, player_mfc):
        """ update player info """
        if isinstance(player_mfc, PlayerMessageFromClient):
            player_mfc.set_player_info(self._player_info)
