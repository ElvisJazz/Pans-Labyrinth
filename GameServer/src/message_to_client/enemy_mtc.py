# ======================================================================
# Function: Message of the enemy which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.enemy_info import EnemyInfo
from constant.message_type import MessageType


class EnemyMessageToClient(object):

    def __init__(self, message_type, target_type, enemy_info):
        if isinstance(enemy_info, EnemyInfo):
            # Set basic information
            self.message_type = message_type
            self.target_type = target_type
            self.enemy_type = enemy_info.enemy_type_id
            self.enemy_id = enemy_info.enemy_id
            # Set message items according to different message type
            if message_type == MessageType.CREATE:
                self.health = enemy_info.health
                self.max_health = enemy_info.max_health
                self.position = enemy_info.position
                self.hurt = enemy_info.hurt
                self.experience = enemy_info.experience
                self.target_position = enemy_info.target_position
                self.action_type = enemy_info.action_type
            elif message_type == MessageType.UPDATE:
                self.target_position = enemy_info.target_position
                self.action_type = enemy_info.action_type
        else:
            raise Exception("Instance of EnemyInfo is expected!")