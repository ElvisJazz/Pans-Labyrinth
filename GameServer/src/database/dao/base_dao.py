# ======================================================================
# Function: Base class of Data Access Object
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.dbcp_manager import DBCPManager


class BaseDao(object):

    def __init__(self, player_id, conn=None, has_own_conn=False):
        if has_own_conn:
            self.conn = DBCPManager.get_connection(player_id)
        elif conn is not None:
            self.set_conn(conn)
        self.player_id = player_id

    def set_conn(self, conn):
        self.conn = conn

    def data_to_object(self, data_tuple):
        pass

    def data_to_list(self, data_list):
        pass

