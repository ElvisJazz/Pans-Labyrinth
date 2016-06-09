# ======================================================================
# Function: Manage information of the scene for scene
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
import json
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.maze_info_bl import MazeInfoBL
from message_to_client.maze_mtc import MazeMessageToClient
import dispatcher
import manager.manager_online


class SceneManager(object):
    def __init__(self, player_id):
        self._player_id = player_id
        self._maze_info = None
        self._maze_array = []
        self._maze_enemy_spawner_list = [] # store tuple like (row, 0, column)
        self._next = 0

    def save(self):
        """save the information of maze"""
        maze_info_bl = MazeInfoBL(self._player_id, None, True)
        flag = maze_info_bl.update_maze(self._maze_info)
        return flag

    def load(self):
        """load the information of maze"""
        maze_info_bl = MazeInfoBL(self._player_id, None, True)
        self._maze_info = maze_info_bl.get_maze()
        # init maze info according to current maze array
        self.init_maze_info()

    def generate(self):
        """ send maze info to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = MazeMessageToClient(MessageType.CREATE, MessageTargetType.SCENE, self._maze_info)
        dispatcher.Dispatcher.send(socket, message)

    def init_maze_info(self):
        l = json.loads(self._maze_info.maze_json)
        for i in range(0, self._maze_info.row):
            t_list = []
            for j in range(0, self._maze_info.column):
                e = l.pop(0)
                t_list.append(e)
                if e["isEnemySpawner"]:
                    self._maze_enemy_spawner_list.append((i*self._maze_info.height, 0, j*self._maze_info.width))
            self._maze_array.append(t_list)

    def get_next_enemy_spawner(self):
        r = self._maze_enemy_spawner_list[self._next]
        self._next = (self._next+1) % len(self._maze_enemy_spawner_list)
        return r