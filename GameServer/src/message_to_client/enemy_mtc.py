# ======================================================================
# Function: Message of the enemy which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.enemy_info import EnemyInfo
from type.message_type import MessageType


class EnemyMessageToClient(object):

    def __init__(self, message_type, enemy_info):
        if isinstance(enemy_info, EnemyInfo):
            # Set basic information
            self._message_type = message_type
            self._enemy_type = enemy_info._enemy_type
            self._enemy_id = enemy_info._enemy_id
            # Set message items according to different message type
            if message_type == MessageType.CREATE:
                self._health = enemy_info._health
                self._max_health = enemy_info._max_health
                self._position = enemy_info._position
                self._hurt = enemy_info._hurt
                self._experience = enemy_info._experience
            elif message_type == MessageType.UPDATE:
                pass
            elif message_type == MessageType.RUN:
                self._target_position = enemy_info._target_position
            elif message_type == MessageType.ATTACK:
                self._target_position = enemy_info._target_position

        else:
            raise Exception("Instance of EnemyInfo is expected!")