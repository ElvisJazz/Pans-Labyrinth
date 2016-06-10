# ======================================================================
# Function: Manage information of the enemy
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
import threading
from constant.enemy_action_type import EnemyActionType
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.enemy_config_info_bl import EnemyConfigInfoBL
from database.bl.enemy_info_bl import EnemyInfoBL
from info.enemy_info import EnemyInfo
from manager.game.player_manager import PlayerManager
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
        self._enemy_config_list = []
        self._alive_enemy_dict = {}
        self._dead_enemy_list = []
        self._id = 0
        self._time = None
        self._max_enemies = 40

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
        # load other properties
        self._routine_generator = RoutineGenerator(self._game_manager.scene_manager.maze_array)
        self._maze_width = self._game_manager.scene_manager.maze_info.width
        self._maze_height = self._game_manager.scene_manager.maze_info.height

        # generate routine
        target_pos = self.transfer_player_pos_to_target_pos()
        for enemy in self._alive_enemy_dict.values():
            enemy.target_routine = self.get_enemy_routine(enemy.position, target_pos)



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

    def _generate_enemy_list(self, enemy_list):
        """ send enemy info list to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = EnemyMessageToClient(MessageType.CREATE, MessageTargetType.ENEMY, enemy_list)
        dispatcher.Dispatcher.send(socket, message)

    def generate_in_time(self):
        """ generate new enemies in fixed time """
        if self._game_manager.is_running :
            # Create enemy list according to config list
            if len(self._alive_enemy_dict)<self._max_enemies:
                # get player position
                target_pos = self.transfer_player_pos_to_target_pos()
                self._id += 1
                enemy_list = []
                for config in self.enemy_config_list:
                    for i in range(config.amount):
                        pos = self._game_manager.scene_manager.get_next_enemy_spawner()
                        enemy = EnemyInfo(self._id, config.type_id, config.max_health, config.max_health, pos, config.hurt,
                                          config.experience)
                        # set routine
                        enemy.target_routine = self.get_enemy_routine(enemy.position, target_pos)
                        self._alive_enemy_dict[self._id] = enemy
                        enemy_list.append(enemy)
                        self._id += 1
                # Send to client
                self._generate_enemy_list(enemy_list)
            # self._time = threading.Timer(60, self.generate_in_time)
            # self._time.start()
            print "hh"

    def get_enemy_routine(self, enemy_position, target_pos):
        start_pos = (int(enemy_position[0]//self._maze_width),int(enemy_position[2]//self._maze_height))
        routine = self._routine_generator.get_routine(start_pos, target_pos)
        r_routine = []
        for pos in routine:
            r_pos = Position(pos[1]*self._maze_width, 0, pos[0]*self._maze_height)
            r_routine.append(r_pos)

        return r_routine

    def transfer_player_pos_to_target_pos(self):
        """ transfer player real position to target position for enemy routine generation"""
        player_position = self._game_manager.player_manager.player_info.position
        player_position = self.fix_negative_pos(player_position)
        return int(player_position[0]//self._maze_width), int(player_position[2]//self._maze_height)

    def fix_negative_pos(self, pos):
        """ if pos(size = 3) has one or more negative component  """
        r_pos = []
        for i in range(0,3):
            x = pos[i] if pos[i] > 0 else 0
            r_pos.append(x)
        return r_pos

    def update_client_enemy(self):
        """ update enemy info to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        self.set_enemy_state()
        message = EnemyMessageToClient(MessageType.UPDATE, MessageTargetType.ENEMY, self._alive_enemy_dict.values())
        dispatcher.Dispatcher.send(socket, message)

    def set_enemy_state(self):
        """  set routine and action of enemy """
        target_pos = self.transfer_player_pos_to_target_pos()
        for enemy in self._alive_enemy_dict.values():
            r_routine = self.get_enemy_routine(enemy.position, target_pos)
            # if position of player is equal to the enemy ,attack!
            if len(r_routine) == 0:
                r_routine.append(self._game_manager.player_manager.player_info.position)
                enemy.action_type = EnemyActionType.ATTACK
                enemy.target_routine = r_routine
            else:
                enemy.action_type = EnemyActionType.RUN
                enemy.target_routine = r_routine

