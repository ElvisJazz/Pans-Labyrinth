# ======================================================================
# Function: Message of the player which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from src.info.player_info import PlayerInfo
from src.type.message_type import MessageType


class PlayerMessageToClient(object):

    def __init__(self, message_type, player_info):
        if isinstance(player_info, PlayerInfo):
            # Set basic information
            self._message_type = message_type
            self._player_id = player_info._player_id
            self._name = player_info._name
            # Set message items according to different message type
            if message_type == MessageType.CREATE:
                self._health = player_info._health
                self._max_health = player_info._max_health
                self._experience = player_info._experience
                self.max_experience = player_info.max_experience
                self._position = player_info._position
                self._weapon_list = player_info._weapon_list
        else:
            raise Exception("Instance of PlayerInfo is expected!")