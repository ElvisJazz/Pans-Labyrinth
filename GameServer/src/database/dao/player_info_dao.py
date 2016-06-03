# ======================================================================
# Function: Data Access Object of PlayerInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dao.base_dao import BaseDao
from info.player_info import PlayerInfo


class PlayerInfoDao(BaseDao):

    def get_by_id(self):
        cursor = self.conn.cursor()
        cursor.execute('select a.player_id, b.type_id, b.level, a.position_x, a.position_y, a.position_z, a.health, b.max_health,'
                            'a.experience, b.max_experience from player_record a, player_type_config b where '
                            'a.player_id=? and a.player_type_id=b.type_id', (self.player_id,))
        o = self.data_to_object(cursor.fetchone())
        cursor.close()
        return o

    def insert(self, player_info):
        cursor = self.conn.cursor()
        cursor.execute('insert into player_record (player_id, player_type_id, health, experience, position_x, position_y, '
                            'position_z) values (?, ?, ?, ?, ?, ?, ?)', (player_info.player_id, player_info.type_id, player_info.health,
                            player_info.experience, player_info.position[0], player_info.position[1], player_info.position[2],))
        r = cursor.rowcount
        cursor.close()
        return r

    def update(self, player_info):
        cursor = self.conn.cursor()
        cursor.execute('update player_record set player_type_id=?, health=?, experience=?, position_x=?, position_y=?,'
                            'position_z=?) where player_id=?', (player_info.type_id, player_info.health, player_info.experience,
                             player_info.position[0], player_info.position[1], player_info.position[2], player_info.player_id,))
        r = cursor.rowcount
        cursor.close()
        return r

    def delete(self):
        cursor = self.conn.cursor()
        cursor.execute('delete from player_record where player_id=?', (self.player_id,))
        r = cursor.rowcount
        cursor.close()
        return r

    def data_to_object(self, data_tuple):
        if data_tuple is not None:
            return PlayerInfo(data_tuple[0],data_tuple[1],data_tuple[2],(data_tuple[3],data_tuple[4],data_tuple[5]),data_tuple[6],
                          data_tuple[7],data_tuple[8],data_tuple[9])
        return None
