# ======================================================================
# Function: Business Logic base class
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================


class BaseBL(object):

    def __init__(self):
        self.dao = None

    # Who deliver conn should close or maintain the conn
    def set_conn(self, conn):
        self.dao.set_conn(conn)

    # # Rollback
    # def rollback(self):
    #     self.dao.rollback()
    #
    # # Commit
    # def commit(self):
    #     self.dao.commit()