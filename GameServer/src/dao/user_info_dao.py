# ======================================================================
# Function: Data Access Object of UserInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
import sqlite3

from config.config_manager import ConfigManager
from dao.base_dao import BaseDao
from user.user_info import UserInfo


class UserInfoDao(BaseDao):

    def __init__(self):
        pass

    def get_count_by_name(self, name):
        self.cursor.execute('select count(*) from user where name=? ', (name,))
        r = self.cursor.fetchone()
        if r is not None:
            return r[0]
        else:
            return 0

    def get_by_name(self, name):
        self.cursor.execute('select * from user where name = ?', (name,))
        return self.data_to_object(self.cursor.fetchone())

    def get_by_id(self, id):
        self.cursor.execute('select * from user where user_id = ?', (id,))
        return self.data_to_object(self.cursor.fetchone())

    def insert(self, name, password):
        self.cursor.execute('insert into user (name, password) values (?, ?)', (name, password,))
        return self.cursor.rowcount

    def data_to_object(self, data_tuple):
        return UserInfo(data_tuple[0],data_tuple[1],data_tuple[2])

    def rollback(self):
        self.conn.rollback()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

