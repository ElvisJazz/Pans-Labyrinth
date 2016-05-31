# ======================================================================
# Function: Data Access Object of WeaponConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.dao.base_dao import BaseDao
from src.info.weapon_info import WeaponInfo


class WeaponConfigInfoDao(BaseDao):

    def get_weapon_config_list(self):
        self.cursor.execute('select * from weapon_type_config')
        return self.data_to_list(self.cursor.fetchall())

    def data_to_list(self, data_list):
        weapon_config_info_list = []
        for data in data_list:
            weapon_config_info_list.append(WeaponInfo(data))
        return weapon_config_info_list
