# ======================================================================
# Function: Data Access Object of UserInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================

from database.dao.base_dao import BaseDao
from info.user_info import UserInfo


class UserInfoDao(BaseDao):

    def get_count_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute('select count(*) from user where name=? ', (name,))
        r = cursor.fetchone()
        cursor.close()
        if r is not None:
            return r[0]
        else:
            return 0

    def get_by_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute('select * from user where name = ?', (name,))
        o = cursor.fetchone()
        if o is not None:
            o = self.data_to_object(o)
        cursor.close()
        return o

    def get_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute('select * from user where user_id = ?', (id,))
        o = self.data_to_object(cursor.fetchone())
        cursor.close()
        return o

    def insert(self, name, password):
        cursor = self.conn.cursor()
        cursor.execute('insert into user (name, password) values (?, ?)', (name, password,))
        r = cursor.rowcount
        cursor.close()
        return r

    def data_to_object(self, data_tuple):
        if data_tuple is not None:
            return UserInfo(data_tuple[0],data_tuple[1],data_tuple[2])
        return None

    def rollback(self):
        self.conn.rollback()


