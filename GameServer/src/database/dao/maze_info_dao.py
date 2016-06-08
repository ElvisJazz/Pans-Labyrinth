# ======================================================================
# Function: Data Access Object of MazeInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dao.base_dao import BaseDao
from info.maze_info import MazeInfo


class MazeInfoDao(BaseDao):

    def get_by_player_id(self):
        cursor = self.conn.cursor()
        cursor.execute('select a.maze_id, a.type_id, b.row, b.column, a.maze_json from maze_record a, maze_type_config b where '
                       'a.player_id = ? and a.type_id=b.type_id',(self.player_id,))
        o = self.data_to_object(cursor.fetchone())
        cursor.close()
        return o

    def insert(self, maze_info):
        cursor = self.conn.cursor()
        cursor.execute('insert into maze_record (player_id, type_id, maze_json) values (?, ?, ?)',
                            (self.player_id, maze_info.type_id, maze_info.maze_json,))
        r = cursor.rowcount
        cursor.close()
        return r

    def update(self, maze_info):
        cursor = self.conn.cursor()
        cursor.execute('update maze_record set type_id=?, maze_json=? where player_id=? and maze_id=?',
                            (maze_info.type_id, maze_info.maze_json,self.player_id, maze_info.maze_id,))
        r = cursor.rowcount
        cursor.close()
        return r

    def delete(self, maze_id):
        cursor = self.conn.cursor()
        cursor.execute('delete from maze_record where player_id=? and maze_id=?', (self.player_id, maze_id,))
        r = cursor.rowcount
        cursor.close()
        return r

    def data_to_object(self, data_tuple):
        if data_tuple is not None:
            return MazeInfo(data_tuple[0],data_tuple[1],data_tuple[2],data_tuple[3],data_tuple[4])
        return None
