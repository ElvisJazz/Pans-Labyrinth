# ======================================================================
# Function: Manage information of the enemy
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
import threading
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.enemy_config_info_bl import EnemyConfigInfoBL
from database.bl.enemy_info_bl import EnemyInfoBL
from info.enemy_info import EnemyInfo
from message_from_client.enemy_mfc import EnemyMessageFromClient
import manager.manager_online
import dispatcher
from message_to_client.enemy_mtc import EnemyMessageToClient


class EnemyManager(object):
    def __init__(self, player_id, game_manager):
        self.game_manager = game_manager
        self._player_id = player_id
        self.enemy_config_list = []
        self._alive_enemy_dict = {}
        self._dead_enemy_list = []
        self._id = 0
        self._time = None

    def save(self):
        """save the information of enemy"""
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        flag = enemy_info_bl.update_dict(self._alive_enemy_dict)
        flag |= enemy_info_bl.delete_list(self._dead_enemy_list)
        return flag

    def load(self):
        """load the information of enemy"""
        # load enemy config
        enemy_config_bl = EnemyConfigInfoBL(self._player_id, None, True)
        self.enemy_config_list = enemy_config_bl.get_list()
        # load alive enemy record
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        (self._alive_enemy_dict, self._id) = enemy_info_bl.get_dict_and_max_id()
        print 1

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
        """ send enemy info to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = EnemyMessageToClient(MessageType.CREATE, MessageTargetType.ENEMY, self._alive_enemy_dict.values())
        dispatcher.Dispatcher.send(socket, message)

    def generate_enemy_list(self, enemy_list):
        """ send enemy info list to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = EnemyMessageToClient(MessageType.CREATE, MessageTargetType.ENEMY, enemy_list)
        dispatcher.Dispatcher.send(socket, message)

    def generate_in_time(self):
        """ generate new enemies in fixed time """
        if self.game_manager.is_running:
            # Create enemy list according to config list
            self._id += 1
            enemy_list = []
            for config in self.enemy_config_list:
                for i in range(config.amount):
                    pos = self.game_manager.scene_manager.get_next_enemy_spawner()
                    enemy = EnemyInfo(self._id, config.type_id, config.max_health, config.max_health, pos, config.hurt,
                                      config.experience)
                    self._alive_enemy_dict[self._id] = enemy
                    enemy_list.append(enemy)
                    self._id += 1
            # Send to client
            self.generate_enemy_list(enemy_list)
            # self._time = threading.Timer(60, self.generate_in_time)
            # self._time.start()
            print "hh"
