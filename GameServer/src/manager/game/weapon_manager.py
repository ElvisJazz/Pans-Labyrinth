# ======================================================================
# Function: Manage information of the weapon
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
import threading

from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.weapon_info_bl import WeaponInfoBL
from message.message_from_client.weapon_mfc import WeaponMessageFromClient
from message.message_to_client.weapon_mtc import WeaponMessageToClient
import manager.manager_online
import dispatcher


class WeaponManager(object):
    def __init__(self, player_id, game_manager):
        self._game_manager = game_manager
        self._player_id = player_id
        self._weapon_dict = {}
        self._time = None

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
            else: # update weapon list
                weapon_mfc.set_weapon_list(self._weapon_dict)

    def generate_default_weapon(self):
        """ generate weapons when player firstly login """
        taken_weapon_list = []
        if len(self._weapon_dict) > 0:
            socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
            for info in self._weapon_dict.values():
                if info.take == 1:
                    taken_weapon_list.append(info)
            message = WeaponMessageToClient(MessageType.CREATE, MessageTargetType.WEAPON, taken_weapon_list)
            dispatcher.Dispatcher.send(socket, message)

    def generate_in_time(self):
        """ generate weapons when game is running """
        untaken_weapon_list = []
        if self._game_manager.is_running and self._weapon_dict != {}:
            socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
            for info in self._weapon_dict.values():
                if info.take == 0 and not info.generate:
                    untaken_weapon_list.append(info)

            if len(untaken_weapon_list) > 0:
                pos = self._game_manager.scene_manager.get_next_enemy_spawner()
                untaken_weapon_list[0].weapon_position = (pos[0], 0.5, pos[2])
                message = WeaponMessageToClient(MessageType.CREATE, MessageTargetType.WEAPON, [untaken_weapon_list[0]])
                untaken_weapon_list[0].generate = True
                dispatcher.Dispatcher.send(socket, message)

                self._time = threading.Timer(15, self.generate_in_time)
                self._time.start()
            print "hh2"
