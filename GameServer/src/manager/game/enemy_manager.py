# ======================================================================
# Function: Manage information of the enemy
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================

from __future__ import division
import math
import threading
from constant.enemy_action_type import EnemyActionType
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.enemy_config_info_bl import EnemyConfigInfoBL
from database.bl.enemy_info_bl import EnemyInfoBL
from database.dbcp_manager import DBCPManager
from info.enemy_info import EnemyInfo
from message_from_client.enemy_mfc import EnemyMessageFromClient
import manager.manager_online
import dispatcher
from message_to_client.enemy_mtc import EnemyMessageToClient
from util.position import Position
from util.routine_generator import RoutineGenerator


class EnemyManager(object):
    def __init__(self, player_id, game_manager):
        self._game_manager = game_manager
        self._player_id = player_id
        self.enemy_config_list = []
        self._alive_enemy_dict = {}
        self._new_enemy_dict = {}
        self._dead_enemy_list = []
        self._id = 0
        self._time = None

    def save(self):
        """save the information of enemy"""
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        enemy_info_bl.add_list(self._new_enemy_dict.values())
        enemy_info_bl.update_dict(self._alive_enemy_dict)
        enemy_info_bl.delete_list(self._dead_enemy_list)
        return True

    def load(self):
        """load the information of enemy"""
        # load enemy config
        enemy_config_bl = EnemyConfigInfoBL(self._player_id, None, True)
        self.enemy_config_list = enemy_config_bl.get_list()
        # load alive enemy record
        enemy_info_bl = EnemyInfoBL(self._player_id, None, True)
        (self._alive_enemy_dict, self._id) = enemy_info_bl.get_dict_and_max_id()
        # load other properties
        self._routine_generator = RoutineGenerator(self._game_manager.scene_manager.maze_array)
        self._maze_width = self._game_manager.scene_manager.maze_info.width
        self._maze_height = self._game_manager.scene_manager.maze_info.height

        # generate routine
        target_pos = self.transfer_player_pos_to_target_pos()
        for enemy in self._alive_enemy_dict.values():
            start_pos = self.transfer_enemy_pos_to_start_pos(enemy.position)
            enemy.target_routine = self.get_enemy_routine(start_pos, target_pos)



    def update(self, enemy_mfc):
        """ update enemy info """
        if isinstance(enemy_mfc, EnemyMessageFromClient):
            id = enemy_mfc.get_enemy_id()
            # message from client is for single enemy
            if id != -1:
                enemy = None
                is_in_alive_dict = False
                if self._alive_enemy_dict.has_key(id):
                    enemy = self._alive_enemy_dict[id]
                    is_in_alive_dict = True
                if enemy is None:
                    enemy = self._new_enemy_dict[id]
                enemy_mfc.set_enemy_info(enemy)
                # if enemy is dead, pop it from dead dict to living list
                if enemy.health <= 0:
                    if is_in_alive_dict:
                        self._alive_enemy_dict.pop(id)
                    else:
                        self._new_enemy_dict.pop(id)
                    self._dead_enemy_list.append(enemy)
                else:
                    # update enemy state, mainly for attack action
                    start_pos = self.transfer_enemy_pos_to_start_pos(enemy.next_position)
                    target_pos = self.transfer_player_pos_to_target_pos()
                    self.__set_enemy_state(enemy, start_pos, target_pos)
                    # send the enemy respond
                    socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
                    l = [enemy]
                    message = EnemyMessageToClient(MessageType.UPDATE, MessageTargetType.ENEMY, l)
                    dispatcher.Dispatcher.send(socket, message)
            # message from client is for enemy list, mainly for planing new routines
            else:
                enemy_mfc.set_enemy_list(self._alive_enemy_dict, self._new_enemy_dict)

    def generate(self):
        """ send enemy info to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = EnemyMessageToClient(MessageType.CREATE, MessageTargetType.ENEMY, self._alive_enemy_dict.values())
        dispatcher.Dispatcher.send(socket, message)

    def _generate_enemy_list(self, enemy_list):
        """ send enemy info list to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = EnemyMessageToClient(MessageType.CREATE, MessageTargetType.ENEMY, enemy_list)
        dispatcher.Dispatcher.send(socket, message)

    def generate_in_time(self):
        """ generate new enemies in fixed time """
        if self._game_manager.is_running :
            # Create enemy list according to config list
            if len(self._alive_enemy_dict)+len(self._new_enemy_dict) == 0:
                # get player position
                target_pos = self.transfer_player_pos_to_target_pos()
                self._id += 1
                enemy_list = []
                for config in self.enemy_config_list:
                    for i in range(config.amount):
                        pos = self._game_manager.scene_manager.get_next_enemy_spawner()
                        enemy = EnemyInfo(self._id, config.type_id, config.max_health, config.max_health, pos, config.hurt,
                                          config.experience, config.attack_distance)
                        # set routine
                        start_pos = self.transfer_enemy_pos_to_start_pos(enemy.position)
                        enemy.target_routine = self.get_enemy_routine(start_pos, target_pos)
                        self._new_enemy_dict[self._id] = enemy
                        enemy_list.append(enemy)
                        self._id += 1
                # Send to client
                self._generate_enemy_list(enemy_list)
                # Need new conn to save because SQLite3 can only use the same connection in the same thread for safe
                # conn = DBCPManager.get_connection()
                # EnemyInfoBL(self._player_id, conn).add_list(enemy_list)
                # conn.commit()
                # conn.close()
            self._time = threading.Timer(15, self.generate_in_time)
            self._time.start()
            print "hh1"

    def get_enemy_routine(self, start_pos, target_pos):
        routine = self._routine_generator.get_routine(start_pos, target_pos)
        r_routine = []
        for pos in routine:
            r_pos = Position(pos[1]*self._maze_width, 0, pos[0]*self._maze_height)
            r_routine.append(r_pos)
        if len(r_routine) > 0:
            r_routine.pop()
            r_routine.append(self.transfer_pos_tuple_to_position_type(self._game_manager.player_manager.player_info.position))
        return r_routine

    def transfer_player_pos_to_target_pos(self):
        """ transfer player real position to target position for enemy routine generation"""
        player_position = self._game_manager.player_manager.player_info.position
        player_position = self.fix_negative_pos(player_position)
        return int(round(player_position[0]/self._maze_width)), int(round(player_position[2]/self._maze_height))

    def transfer_enemy_pos_to_start_pos(self, enemy_position):
        """ transfer enemy real position to start position for enemy routine generation"""
        enemy_position = self.fix_negative_pos(enemy_position)
        return int(round(enemy_position[0]/self._maze_width)), int(round(enemy_position[2]/self._maze_height))

    def fix_negative_pos(self, pos):
        """ if pos(size = 3) has one or more negative component  """
        r_pos = []
        try:
            for i in range(0, 3):
                x = pos[i] if pos[i] > 0 else 0
                r_pos.append(x)
        except Exception,e:
            print e
        return r_pos

    def update_client_enemy_routine(self):
        """ update enemy info to client, mainly routines """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        self.__set_enemies_state()
        enemy_list = self._alive_enemy_dict.values()
        enemy_list.extend(self._new_enemy_dict.values())
        message = EnemyMessageToClient(MessageType.UPDATE, MessageTargetType.ENEMY, enemy_list)
        dispatcher.Dispatcher.send(socket, message)

    def __set_enemies_state(self):
        """  set routine and action of enemy """
        target_pos = self.transfer_player_pos_to_target_pos()
        enemy_list = self._alive_enemy_dict.values()
        enemy_list.extend(self._new_enemy_dict.values())
        for enemy in enemy_list:
            enemy_pos = enemy.next_position if enemy.next_position is not None else enemy.position
            start_pos = self.transfer_enemy_pos_to_start_pos(enemy_pos)
            self.__set_enemy_state(enemy, start_pos, target_pos)

    def __set_enemy_state(self, enemy, start_pos, target_pos):
        r_routine = self.get_enemy_routine(start_pos, target_pos)
        # if position of player is equal to the enemy ,attack!
        if len(r_routine) == 0:
            r_routine.append(self.transfer_pos_tuple_to_position_type(self._game_manager.player_manager.player_info.position))
        if self.in_attack_distance_between_enemy_and_player(enemy):
            enemy.action_type = EnemyActionType.ATTACK
            enemy.target_routine = r_routine
        else:
            enemy.action_type = EnemyActionType.RUN
            enemy.target_routine = r_routine

    def transfer_pos_tuple_to_position_type(self, pos):
        """
        :param pos:(0,1,2)
        :return:position: x=0, y=1, z=2
        """
        return Position(pos[0], pos[1], pos[2])

    def in_attack_distance_between_enemy_and_player(self, enemy):
        pos1 = self._game_manager.player_manager.player_info.position
        pos2 = enemy.position
        return math.pow(pos1[0]-pos2[0],2)+math.pow(pos1[2]-pos2[2],2) <= enemy.attack_distance_square
