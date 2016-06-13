# ======================================================================
# Function: Message of the maze which is sent to client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
import json
from info.maze_info import MazeInfo
from constant.message_type import MessageType


class MazeMessageToClient(object):

    def __init__(self, message_type, target_type, maze_info):
        if isinstance(maze_info, MazeInfo):
            # Set basic information
            self.message_type = message_type
            self.target_type = target_type
            # Set message items according to different message type
            if message_type == MessageType.CREATE:
                self.maze_array = json.loads(maze_info.maze_json)
                self.row = maze_info.row
                self.column = maze_info.column
        else:
            raise Exception("Instance of MazeInfo is expected!")