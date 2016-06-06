# ======================================================================
# Function: Manage information of the weapon
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.weapon_info_bl import WeaponInfoBL
from database.dbcp_manager import DBCPManager
from dispatcher import Dispatcher
from manager.manager_online import OnlineManager
from message_from_client.weapon_mfc import WeaponMessageFromClient
from message_to_client.weapon_mtc import WeaponMessageToClient


class WeaponManager(object):
    def __init__(self, player_id):
        self._player_id = player_id
        self._weapon_dict = {}

    def save(self):
        """save the information of weapon"""
        weapon_info_bl = WeaponInfoBL(self._player_id, None, True)
        flag = weapon_info_bl.update_dict(self._weapon_dict)
        return flag

    def load(self):
        """load the information of weapon"""
        weapon_info_bl = WeaponInfoBL(self._player_id, None, True)
        self._weapon_dict = weapon_info_bl.get_dict()

    def update(self, weapon_mfc):
        """ update enemy info """
        if isinstance(weapon_mfc, WeaponMessageFromClient):
            id = weapon_mfc.get_weapon_id()
            if id != -1:
                weapon_mfc.set_weapon_info(self._weapon_dict[id])

    def generate_default_weapon(self):
        """ generate weapons when player login """
        taken_weapon_list = []
        if self._weapon_dict != {}:
            socket = OnlineManager.socket_buffer[self._player_id]
            for info in self._weapon_dict.values():
                if info.take == 1:
                    taken_weapon_list.append(info)
            message = ""
            if taken_weapon_list is []:
                message = WeaponMessageToClient(MessageType.CREATE, MessageTargetType.WEAPON, self._weapon_dict.values()[0])
                self._weapon_dict.values()[0].generate = True
            else:
                message = WeaponMessageToClient(MessageType.CREATE, MessageTargetType.WEAPON, taken_weapon_list[0])
            Dispatcher.send(socket, message)

    def generate_weapon(self):
        """ generate weapons when game is running """
        untaken_weapon_list = []
        if self._weapon_dict != {}:
            socket = OnlineManager.socket_buffer[self._player_id]
            for info in self._weapon_dict.values():
                if info.take == 0 and not info.generat:
                    untaken_weapon_list.append(info)

            if untaken_weapon_list is not []:
                message = WeaponMessageToClient(MessageType.CREATE, MessageTargetType.WEAPON, untaken_weapon_list[0])
                untaken_weapon_list[0].generate = True
                Dispatcher.send(socket, message)
