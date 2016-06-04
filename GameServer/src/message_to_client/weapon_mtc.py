# ======================================================================
# Function: Message of the weapon which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.weapon_info import WeaponInfo
from constant.message_type import MessageType


class WeaponMessageToClient(object):

    def __init__(self, message_type, target_type, weapon_info):
        if isinstance(weapon_info, WeaponInfo):
            # Set basic information
            self.message_type = message_type
            self.target_type = target_type
            # Set message items according to different message type
            if message_type == MessageType.CREATE:
                self.type_id = weapon_info.weapon_type_id
                self.position = weapon_info.weapon_position
                self.take = weapon_info.take
                self.current_bullets_in_gun = weapon_info.current_bullets_in_gun
                self.current_bullets_in_bag = weapon_info.current_bullets_in_bag
                self.max_bullets_in_gun = weapon_info.max_bullets_in_gun
                self.max_bullets_in_bag = weapon_info.max_bullets_in_bag
        else:
            raise Exception("Instance of WeaponInfo is expected!")