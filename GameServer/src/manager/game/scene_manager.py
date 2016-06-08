# ======================================================================
# Function: Manage information of the scene for scene
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from database.bl.maze_info_bl import MazeInfoBL
from message_to_client.maze_mtc import MazeMessageToClient
import dispatcher
import manager.manager_online


class SceneManager(object):
    def __init__(self, player_id):
        self._player_id = player_id
        self._scene_info = None

    def save(self):
        """save the information of maze"""
        maze_info_bl = MazeInfoBL(self._player_id, None, True)
        flag = maze_info_bl.update_maze(self._scene_info)
        return flag

    def load(self):
        """load the information of maze"""
        maze_info_bl = MazeInfoBL(self._player_id, None, True)
        self._scene_info = maze_info_bl.get_maze()

    def generate(self):
        """ send maze info to client """
        socket = manager.manager_online.OnlineManager.socket_buffer[self._player_id]
        message = MazeMessageToClient(MessageType.CREATE, MessageTargetType.SCENE, self._scene_info)
        dispatcher.Dispatcher.send(socket, message)
