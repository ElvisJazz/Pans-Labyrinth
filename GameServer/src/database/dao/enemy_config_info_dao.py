# ======================================================================
# Function: Data Access Object of EnemyConfigInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dao.base_dao import BaseDao
from info.enemy_config_info import EnemyConfigInfo


class EnemyConfigInfoDao(BaseDao):

    def get_enemy_config_list(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from enemy_type_config')
        l = self.data_to_list(cursor.fetchall())
        cursor.close()
        return l

    def data_to_list(self, data_list):
        enemy_config_info_list = []
        if len(data_list) > 0:
            for data in data_list:
                enemy_config_info_list.append(EnemyConfigInfo(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        return enemy_config_info_list
