# ======================================================================
# Function: Manage information of the enemy
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.enemy_info_bl import EnemyInfoBL
from message_from_client.enemy_mfc import EnemyMessageFromClient
import manager.manager_online
import dispatcher
from message_to_client.enemy_mtc import EnemyMessageToClient


class EnemyManager(object):
    def __init__(self, player_id):
        self._player_id = player_id
        self._alive_enemy_dict = {}
        self._dead_enemy_list = []

    def save(self):
        """save the information of enemy"""
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        flag = enemy_info_bl.update_dict(self._alive_enemy_dict)
        flag |= enemy_info_bl.delete_list(self._dead_enemy_list)
        return flag

    def load(self):
        """load the information of enemy"""
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        self._alive_enemy_dict = enemy_info_bl.get_dict()

    def update(self, enemy_mfc):
        """ update enemy info """
        if isinstance(enemy_mfc, EnemyMessageFromClient):
            id = enemy_mfc.get_enemy_id()
            if id != -1:
                enemy_mfc.set_enemy_info(self._alive_enemy_dict[id])
                # if enemy is dead, pop it from dead dict to living list
                if self._alive_enemy_dict[id].health <= 0:
                    self._dead_enemy_list.append(self._alive_enemy_dict.pop(id))

    def generate(self):
        """ send player info to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = EnemyMessageToClient(MessageType.CREATE, MessageTargetType.ENEMY, self._alive_enemy_dict.values())
        dispatcher.Dispatcher.send(socket, message)