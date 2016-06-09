# ======================================================================
# Function: Data Access Object of WeaponInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dao.base_dao import BaseDao
from info.weapon_info import WeaponInfo


class WeaponInfoDao(BaseDao):

    def get_dict_by_player_id(self):
        cursor = self.conn.cursor()
        cursor.execute('select a.weapon_id, b.type_id, b.weapon_type, a.take, a.current_bullets_in_gun, a.current_bullets_in_bag,'
                            'b.max_bullets_in_gun, b.max_bullets_in_bag, a.position_x, a.position_y, a.position_z, b.hurt, b.default0 '
                            'from weapon_record a, weapon_type_config b where a.player_id = ? and a.weapon_type_id=b.type_id',
                            (self.player_id,))
        d = self.data_to_dict(cursor.fetchall())
        cursor.close()
        return d

    def insert(self, weapon_info):
        cursor = self.conn.cursor()
        cursor.execute('insert into weapon_record (player_id, weapon_type_id, take, current_bullets_in_gun,'
                            'current_bullets_in_bag, position_x, position_y, position_z) values (?, ?, ?, ?, ?, ?, ?, ?)',
                            (self.player_id, weapon_info.weapon_type_id, weapon_info.take, weapon_info.current_bullets_in_gun,weapon_info.current_bullets_in_bag, weapon_info.weapon_position[0], weapon_info.weapon_position[1], weapon_info.weapon_position[2],))
        r = cursor.rowcount
        cursor.close()
        return r

    def update(self, weapon_info):
        cursor = self.conn.cursor()
        cursor.execute('update weapon_record set take=?, current_bullets_in_gun=?, current_bullets_in_bag=?,'
                            'position_x=?, position_y=?, position_z=? where player_id=? and weapon_id=?',
                            (weapon_info.take, weapon_info.current_bullets_in_gun, weapon_info.current_bullets_in_bag,
                             weapon_info.position[0], weapon_info.position[1],weapon_info.position[2],self.player_id, weapon_info.weapon_id,))
        r = cursor.rowcount
        cursor.close()
        return r

    def delete(self, weapon_id):
        cursor = self.conn.cursor()
        cursor.execute('delete from enemy_record where player_id=? and weapon_id=?', (self.player_id, weapon_id,))
        r = cursor.rowcount
        cursor.close()
        return r

    def data_to_dict(self, data_list):
        weapon_info_dict = {}
        if len(data_list) > 0:
            for data in data_list:
                weapon_info_dict[data[0]] = WeaponInfo(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],(data[8],data[9],data[10]), data[11], data[12])
        return weapon_info_dict
