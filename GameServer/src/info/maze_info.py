# ======================================================================
# Function: Store information of the maze
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================


class MazeInfo(object):

    def __init__(self, maze_id, type_id, row, column, maze_json):
        self.maze_id = maze_id
        self.type_id = type_id
        self.maze_json = maze_json
        self.row = row
        self.column = column

