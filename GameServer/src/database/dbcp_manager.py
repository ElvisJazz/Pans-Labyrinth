# ======================================================================
# Function: Manage data base connection pool
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
import sqlite3
from src.config.config_manager import ConfigManager


class DBCPManager(object):

    # default connection
    __default_conn = None
    # connection dict
    __conn_dict = {}

    @classmethod
    def init(cls):
        cls.__default_conn = sqlite3.connect(ConfigManager.DB_file)
        cls.__conn_dict[ConfigManager.DB_file] = cls.__default_conn

    @classmethod
    def get_connection(cls, db_file=''):
        if db_file == '':
            return cls.__default_conn
        elif cls.__conn_dict.has_key(db_file):
            return cls.__conn_dict[db_file]
        else:
            cls.__conn_dict[db_file] = sqlite3.connect(db_file)
            return cls.__conn_dict[db_file]

    @classmethod
    def close_conn(cls, db_file):
        if ConfigManager.DB_file == db_file:
            cls.__conn_dict.pop(db_file)
            cls.__default_conn.close()
            cls.__default_conn = None
        elif cls.__conn_dict.has_key(db_file):
            cls.__conn_dict[db_file].close()
            cls.__conn_dict.pop(db_file)

    @classmethod
    def close_all_conn(cls):
        for db_file in cls.__conn_dict:
            cls.__conn_dict[db_file].close()
            cls.__conn_dict.pop(db_file)
        cls.__default_conn = None

    @classmethod
    def destroy(cls):
        cls.close_all()