# ======================================================================
# Function: Message of the player which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.player_info import PlayerInfo
from constant.message_type import MessageType


class PlayerMessageToClient(object):

    def __init__(self, message_type, target_type, player_info):
        if isinstance(player_info, PlayerInfo):
            # Set basic information
            self.message_type = message_type
            self.target_type = target_type
            self.player_id = player_info.player_id
            # Set message items according to different message type
            if message_type == MessageType.UPDATE:
                self.health = player_info.health
                self.max_health = player_info.max_health
                self.experience = player_info.experience
                self.max_experience = player_info.max_experience
                self.position = player_info.position
        else:
            raise Exception("Instance of PlayerInfo is expected!")