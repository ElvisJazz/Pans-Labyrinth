# ======================================================================
# Function: Data Access Object of EnemyInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.dao.base_dao import BaseDao
from src.info.enemy_info import EnemyInfo


class EnemyInfoDao(BaseDao):

    def get_list_by_player_id(self, player_id):
        self.cursor.execute('select a.enemy_id, a.enemy_type_id, a.health, b.max_health, a.position_x, a.position_y, '
                            'a.position_z, b.hurt, b.experience from enemy_record a, enemy_type_config b '
                            'where a.player_id = ? and a.enemy_type_id=b.type_id', (player_id,))
        return self.data_to_list(self.cursor.fetchall())

    def insert(self, player_id, enemy_info):
        self.cursor.execute('insert into enemy_record (player_id, enemy_id, enemy_type_id, health, position_x, '
                            'position_y, position_z) values (?, ?, ?, ?, ?, ?, ?,)', (player_id, enemy_info.enemy_id,
                            enemy_info.enemy_type, enemy_info.health, enemy_info.position[0], enemy_info.position[1],
                            enemy_info.position[2],))
        return self.cursor.rowcount

    def update(self, player_id, enemy_info):
        self.cursor.execute('update enemy_record set health=?, position_x=?, position_y=?, position_z=?) where '
                            'player_id=? and enemy_id=?', (enemy_info.health, enemy_info.position[0], enemy_info.position[1],
                            enemy_info.position[2], player_id, enemy_info.enemy_id,))
        return self.cursor.rowcount

    def delete(self, player_id, enemy_info):
        self.cursor.execute('delete from enemy_record where player_id=? and enemy_id=?', (player_id, enemy_info.enemy_id,))
        return self.cursor.rowcount

    def data_to_list(self, data_list):
        enemy_info_list = []
        for data in data_list:
            enemy_info_list.append(EnemyInfo(data))
        return enemy_info_list
