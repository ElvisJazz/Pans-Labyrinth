# ======================================================================
# Function: Message of the player which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from src.info.player_info import PlayerInfo


class PlayerMessageFromClient(object):

    def __init__(self):
        pass;

    def set_player_info(self, player_info):
        if isinstance(player_info, PlayerInfo):
            if hasattr(self, '_player_id'):
                player_info._player_id = self._player_id
            elif hasattr(self, '_position'):
                player_info._position = self._position
            elif hasattr(self, '_health'):
                player_info._health = self._health
            elif hasattr(self, '_experience'):
                player_info._experience = self._experience
            elif hasattr(self, '_weapon_list'):
                player_info._weapon_list = self._weapon_list
        else:
            raise Exception("Instance of PlayerInfo is expected!")