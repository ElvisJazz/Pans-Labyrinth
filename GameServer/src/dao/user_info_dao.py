# ======================================================================
# Function: Data Access Object of UserInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
import sqlite3
from src.config.config_manager import ConfigManager
from src.dao.base_dao import BaseDao
from src.user.user_info import UserInfo


class UserInfoDao(object):

    def __init__(self):
        self.conn = sqlite3.connect(ConfigManager.DB_file)
        self.cursor = self.conn.cursor()

    def get_count_by_name(self, name):
        return self.cursor.execute('select count(*) from user where name = ?', (name,))

    def get_by_name(self, name):
        self.cursor.execute('select * from user where name = ?', (name,))
        return self.data_to_object(self.cursor.fetchone())

    def get_by_id(self, id):
        self.cursor.execute('select * from user where user_id = ?', (id,))
        return self.data_to_object(self.cursor.fetchall()[0])

    def insert(self, name, password):
        self.cursor.execute('insert into user (name, password) values (?, ?)', (name, password,))
        return self.cursor.rowcount

    def data_to_object(self, data_tuple):
        return UserInfo(data_tuple)

    def rollback(self):
        self.conn.rollback()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

