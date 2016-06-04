# ======================================================================
# Function: Message of the player which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.player_info import PlayerInfo


class PlayerMessageFromClient(object):

    def set_player_info(self, player_info):
        if isinstance(player_info, PlayerInfo):
            if hasattr(self, 'player_id'):
                player_info.player_id = self.player_id
            if hasattr(self, 'position'):
                player_info.position = self.position
            if hasattr(self, 'health'):
                player_info.health = self.health
            if hasattr(self, 'experience'):
                player_info.experience = self.experience
        else:
            raise Exception("Instance of PlayerInfo is expected!")