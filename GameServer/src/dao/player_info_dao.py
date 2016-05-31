# ======================================================================
# Function: Data Access Object of PlayerInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.dao.base_dao import BaseDao
from src.info.player_info import PlayerInfo


class PlayerInfoDao(BaseDao):

    def get_by_id(self):
        self.cursor.execute('select a.player_id, b.type_id, b.level, a.position_x, a.position_y, a.position_z, a.health, b.max_health'
                            'a.experience, b.max_experience,  from player_record a, player_type_config b where '
                            'a.player_id=? and a.player_type_id=b.type_id', (self.player_id,))
        return self.data_to_object(self.cursor.fetcheone())

    def insert(self, player_info):
        self.cursor.execute('insert into player_record (player_id, player_type_id, health, experience, position_x, position_y, '
                            'position_z) values (?, ?, ?, ?, ?, ?, ?)', (player_info.player_id,player_info.player_type_id, player_info.health,
                            player_info.experience, player_info.position[0], player_info.position[1], player_info.position[2],))
        return self.cursor.rowcount

    def update(self, player_info):
        self.cursor.execute('update player_record set player_type_id=?, health=?, experience=?, position_x=?, position_y=?,'
                            'position_z=?) where player_id=?', (player_info.type_id, player_info.health, player_info.experience,
                             player_info.position[0], player_info.position[1], player_info.position[2], player_info.player_id,))
        return self.cursor.rowcount

    def delete(self):
        self.cursor.execute('delete from player_record where player_id=?', (self.player_id,))
        return self.cursor.rowcount

    def data_to_object(self, data_tuple):
        return PlayerInfo(data_tuple)
