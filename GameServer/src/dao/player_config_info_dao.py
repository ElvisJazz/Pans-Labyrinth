# ======================================================================
# Function: Data Access Object of PlayerConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.dao.base_dao import BaseDao
from src.info.player_config_info import PlayerConfigInfo


class PlayerConfigInfoDao(BaseDao):

    def get_player_config_by_id(self, id):
        self.cursor.execute('select * from player_type_config where type_id=?', (id,))
        return self.data_to_object(self.cursor.fetchall()[0])

    def data_to_object(self, data_tuple):
        return PlayerConfigInfo(data_tuple)
