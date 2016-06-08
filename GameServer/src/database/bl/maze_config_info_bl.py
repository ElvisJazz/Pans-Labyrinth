# ======================================================================
# Function: Business Logic of MazeConfigInfo
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.maze_config_info_dao import MazeConfigInfoDao


class MazeConfigInfoBL(BaseBL):

    def __init__(self, player_id, conn=None, has_own_conn=False):
        self.dao = MazeConfigInfoDao(player_id, conn, has_own_conn)

    # Get maze config list
    def get_list(self):
        return self.dao.get_maze_config_list()