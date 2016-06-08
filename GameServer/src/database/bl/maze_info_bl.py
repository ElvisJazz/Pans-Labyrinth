# ======================================================================
# Function: Business Logic of MazeInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.maze_info_dao import MazeInfoDao

class MazeInfoBL(BaseBL):

    def __init__(self, player_id, conn=None, has_own_conn=False):
            self.dao = MazeInfoDao(player_id, conn, has_own_conn)

    # Get maze info
    def get_maze(self):
        return self.dao.get_by_player_id()

    # Add maze
    def add_maze(self, maze_info):
        rc = self.dao.insert(maze_info)
        #self.dao.commit()
        return rc > 0

    # Update maze
    def update_maze(self, maze_info):
        rc = self.dao.update(maze_info)
        #self.dao.commit()
        return rc > 0

    # Delete maze
    def delete_maze(self, maze_info):
        rc = self.dao.delete(maze_info)
        #self.dao.commit()
        return rc > 0