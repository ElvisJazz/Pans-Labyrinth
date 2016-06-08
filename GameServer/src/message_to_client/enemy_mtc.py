# ======================================================================
# Function: Message of the enemy which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.enemy_info import EnemyInfo
from constant.message_type import MessageType
from message_to_client.empty import Empty


class EnemyMessageToClient(object):

    def __init__(self, message_type, target_type, enemy_info_list):
        self.enemy_info_list = []
        for enemy_info in enemy_info_list:
            if isinstance(enemy_info, EnemyInfo):
                e = Empty()
                # Set basic information
                self.message_type = message_type
                self.target_type = target_type
                e.enemy_type = enemy_info.enemy_type_id
                e.enemy_id = enemy_info.enemy_id
                # Set message items according to different message type
                if message_type == MessageType.CREATE:
                    e.health = enemy_info.health
                    e.max_health = enemy_info.max_health
                    e.position = enemy_info.position
                    e.hurt = enemy_info.hurt
                    e.experience = enemy_info.experience
                    e.target_position = enemy_info.target_position
                    e.action_type = enemy_info.action_type
                elif message_type == MessageType.UPDATE:
                    e.target_position = enemy_info.target_position
                    e.action_type = enemy_info.action_type
                self.enemy_info_list.append(e)
            else:
                raise Exception("Instance of EnemyInfo is expected!")