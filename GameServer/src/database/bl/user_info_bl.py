# ======================================================================
# Function: Business Logic of UserInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from database.bl.base_bl import BaseBL
from database.dao.user_info_dao import UserInfoDao


class UserInfoBL(BaseBL):

    def __init__(self, player_id=0, conn=None, has_own_conn=False):
        self.dao = UserInfoDao(player_id, conn, has_own_conn)

    # Check user exist
    def check_exist(self, name):
        r = self.dao.get_count_by_name(name)
        if r > 0:
            return True
        return False

    # Get user info by name
    def get_user_by_name(self, name):
        return self.dao.get_by_name(name)

    # Get user info by id
    def get_user_by_id(self, id):
        return self.dao.get_by_id(id)

    # Add user info
    def add_user(self, name, password):
        rc = self.dao.insert(name, password)
        #self.dao.commit()
        return rc > 0

    # Rollback
    def rollback(self):
        self.dao.rollback()

    # Commit
    def commit(self):
        self.dao.commit()