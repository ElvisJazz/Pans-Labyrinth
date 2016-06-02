# ======================================================================
# Function: Data Access Object of WeaponInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from dao.base_dao import BaseDao
from info.weapon_info import WeaponInfo


class WeaponInfoDao(BaseDao):

    def get_list_by_player_id(self):
        self.cursor.execute('select a.weapon_id, b.weapon_type_id, a.take, a.current_bullets_in_gun, a.current_bullets_in_bag,'
                            'b.max_bullets_in_gun, b.max_bullets_in_bag, a.position_x, a.position_y, a.position_z, b.hurt,'
                            'from weapon_record a, weapon_type_config b where a.player_id = ? and a.weapon_type_id=b.type_id',
                            (self.player_id,))
        return self.data_to_list(self.cursor.fetchall())

    def insert(self, weapon_info):
        self.cursor.execute('insert into weapon_record (player_id, weapon_type_id, take, current_bullets_in_gun,'
                            'current_bullets_in_bag, position_x, position_y, position_z) values (?, ?, ?, ?, ?, ?, ?, ?)',
                            (self.player_id, weapon_info.weapon_type_id, weapon_info.take, weapon_info.current_bullets_in_gun,weapon_info.current_bullets_in_bag, weapon_info.weapon_position[0], weapon_info.weapon_position[1], weapon_info.weapon_position[2],))
        return self.cursor.rowcount

    def update(self, weapon_info):
        self.cursor.execute('update weapon_record set take=?, current_bullets_in_gun=?, current_bullets_in_bag=?,'
                            'position_x=?, position_y=?, position_z=?) where player_id=? and weapon_id=?',
                            (weapon_info.take, weapon_info.current_bullets_in_gun, weapon_info.current_bullets_in_bag,
                             weapon_info.position[0], weapon_info.position[1],weapon_info.position[2],self.player_id, weapon_info.weapon_id,))
        return self.cursor.rowcount

    def delete(self, weapon_id):
        self.cursor.execute('delete from enemy_record where player_id=? and weapon_id=?', (self.player_id, weapon_id,))
        return self.cursor.rowcount

    def data_to_list(self, data_list):
        weapon_info_list = []
        for data in data_list:
            weapon_info_list.append(WeaponInfo(data[0],data[1],data[2],data[3],data[4],data[5],data[6],(data[7],data[8],data[9]),data[10]))
        return weapon_info_list
