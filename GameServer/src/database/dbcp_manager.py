# ======================================================================
# Function: Manage data base connection pool
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
import sqlite3
from src.config.config_manager import ConfigManager


class DBCPManager(object):

    # free connection list
    free_conn_list = []
    # busy connection dict
    busy_conn_dict = {}
    # max connections
    MAX_CONNS = 100

    @classmethod
    def get_connection(cls, user_id):
        if cls.busy_conn_dict.has_key(user_id):
            return cls.busy_conn_dict[user_id]
        elif len(cls.free_conn_list)+len(cls.busy_conn_dict) < cls.MAX_CONNS:
            if len(cls.free_conn_list) > 0:
                cls.busy_conn_dict[user_id] = cls.free_conn_list.pop(0)
            else:
                cls.busy_conn_dict[user_id] = sqlite3.connect(ConfigManager.DB_file)
            return cls.busy_conn_dict[user_id]
        return None

    @classmethod
    def close_conn(cls, user_id):
        conn = cls.busy_conn_dict.pop(user_id)
        if conn is not None:
            cls.free_conn_list.append(conn)

    @classmethod
    def close_all_conn(cls):
        for conn in cls.free_conn_list:
            conn.close()
        for key in cls.busy_conn_dict:
            cls.busy_conn_dict[key].close()
        cls.free_conn_list = []
        cls.busy_conn_dict = {}

    @classmethod
    def destroy(cls):
        cls.close_all_conn()