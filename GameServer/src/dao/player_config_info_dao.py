# ======================================================================
# Function: Data Access Object of PlayerConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from dao.base_dao import BaseDao
from info.player_config_info import PlayerConfigInfo


class PlayerConfigInfoDao(BaseDao):

    def get_player_config_by_id(self, id):
        self.cursor.execute('select * from player_type_config where type_id=?', (id,))
        return self.data_to_object(self.cursor.fetchone())

    def data_to_object(self, data_tuple):
        return PlayerConfigInfo(data_tuple[0],data_tuple[1],data_tuple[2],data_tuple[3])
