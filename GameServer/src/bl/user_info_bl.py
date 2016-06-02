# ======================================================================
# Function: Business Logic of UserInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from bl.base_bl import BaseBL
from dao.user_info_dao import UserInfoDao


class UserInfoBL(BaseBL):

    def __init__(self):
        self.dao = UserInfoDao()

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
