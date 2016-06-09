# ======================================================================
# Function: Data Access Object of WeaponConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dao.base_dao import BaseDao
from info.weapon_config_info import WeaponConfigInfo


class WeaponConfigInfoDao(BaseDao):

    def get_weapon_config_list(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from weapon_type_config')
        l = self.data_to_list(cursor.fetchall())
        cursor.close()
        return l

    def data_to_list(self, data_list):
        weapon_config_info_list = []
        if len(data_list) > 0:
            for data in data_list:
                weapon_config_info_list.append(WeaponConfigInfo(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
        return weapon_config_info_list
