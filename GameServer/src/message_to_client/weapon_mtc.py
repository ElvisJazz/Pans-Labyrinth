# ======================================================================
# Function: Message of the weapon which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.weapon_info import WeaponInfo
from type.message_type import MessageType


class WeaponMessageToClient(object):

    def __init__(self, message_type, weapon_info):
        if isinstance(weapon_info, WeaponInfo):
            # Set basic information
            self._message_type = message_type
            # Set message items according to different message type
            if message_type == MessageType.CREATE:
                self._weapon_type = weapon_info._weapon_type
                self._current_bullets_in_gun = weapon_info._current_bullets_in_gun
                self._current_bullets_in_bag = weapon_info._current_bullets_in_bag
                self._max_bullets_in_gun = weapon_info._max_bullets_in_gun
                self._max_bullets_in_bag = weapon_info._max_bullets_in_bag
        else:
            raise Exception("Instance of WeaponInfo is expected!")