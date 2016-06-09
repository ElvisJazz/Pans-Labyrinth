# ======================================================================
# Function: Data Access Object of MazeConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dao.base_dao import BaseDao
from info.maze_config_info import MazeConfigInfo


class MazeConfigInfoDao(BaseDao):

    def get_maze_config_list(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from maze_type_config')
        l = self.data_to_list(cursor.fetchall())
        cursor.close()
        return l

    def data_to_list(self, data_list):
        maze_config_info_list = []
        if len(data_list) > 0:
            for data in data_list:
                maze_config_info_list.append(MazeConfigInfo(data[0],data[1],data[2],data[3],data[4],data[5]))
        return maze_config_info_list
