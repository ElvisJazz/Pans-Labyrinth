# ======================================================================
# Function: Base class of Data Access Object
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.database.dbcp_manager import DBCPManager


class BaseDao(object):

    def __init__(self, player_id):
        self.conn = DBCPManager.get_connection(player_id)
        self.cursor = self.conn.cursor()
        self.player_id = player_id

    def data_to_object(self, data_tuple):
        pass

    def data_to_list(self, data_list):
        pass

    def commit(self):
        self.cursor.commit()

    def __del__(self):
        self.cursor.close()