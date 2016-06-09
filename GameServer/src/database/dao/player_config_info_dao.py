# ======================================================================
# Function: Data Access Object of PlayerConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dao.base_dao import BaseDao
from info.player_config_info import PlayerConfigInfo


class PlayerConfigInfoDao(BaseDao):

    def get_player_config_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute('select * from player_type_config where type_id=?', (id,))
        o = self.data_to_object(cursor.fetchone())
        cursor.close()
        return o

    def data_to_object(self, data_tuple):
        if len(data_tuple) > 0:
            return PlayerConfigInfo(data_tuple[0],data_tuple[1],data_tuple[2],data_tuple[3])
        return None
