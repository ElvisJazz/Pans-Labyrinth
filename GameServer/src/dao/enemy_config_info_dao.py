# ======================================================================
# Function: Data Access Object of EnemyConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from dao.base_dao import BaseDao
from info.enemy_config_info import EnemyConfigInfo
from info.enemy_info import EnemyInfo


class EnemyConfigInfoDao(BaseDao):

    def get_enemy_config_list(self):
        self.cursor.execute('select * from enemy_type_config')
        return self.data_to_list(self.cursor.fetchall())

    def data_to_list(self, data_list):
        enemy_config_info_list = []
        for data in data_list:
            enemy_config_info_list.append(EnemyConfigInfo(data[0], data[1], data[2], data[3], data[4], data[5]))
        return enemy_config_info_list
