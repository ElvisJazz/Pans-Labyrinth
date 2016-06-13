# ======================================================================
# Function: Message of the weapon which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.weapon_info import WeaponInfo
from constant.message_type import MessageType
from message.message_to_client.empty import Empty


class WeaponMessageToClient(object):

    def __init__(self, message_type, target_type, weapon_info_list):
        self.weapon_info_list = []
        for weapon_info in weapon_info_list:
            if isinstance(weapon_info, WeaponInfo):
                # Set basic information
                self.message_type = message_type
                self.target_type = target_type
                e = Empty()
                # Set message items according to different message type
                if message_type == MessageType.CREATE:
                    e.name = weapon_info.name
                    e.weapon_id = weapon_info.weapon_id
                    e.type_id = weapon_info.weapon_type_id
                    e.position = weapon_info.weapon_position
                    e.take = weapon_info.take
                    e.current_bullets_in_gun = weapon_info.current_bullets_in_gun
                    e.current_bullets_in_bag = weapon_info.current_bullets_in_bag
                    e.max_bullets_in_gun = weapon_info.max_bullets_in_gun
                    e.max_bullets_in_bag = weapon_info.max_bullets_in_bag
                    self.weapon_info_list.append(e)
            else:
                raise Exception("Instance of WeaponInfo is expected!")