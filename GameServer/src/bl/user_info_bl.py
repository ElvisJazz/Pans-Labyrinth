# ======================================================================
# Function: Business Logic of UserInfo
# Author: Elvis Jia
# Date: 2016.5.30
# ======================================================================
from src.dao.user_info_dao import UserInfoDao


class UserInfoBL(object):

    def __init__(self):
        self.dao = UserInfoDao()

    # Check user exist
    def check_exist(self, name):
        r = self.dao.get_count_by_name(name)
        if r > 0:
            raise Exception('The username has existed!')
        return True

    # Get user info by name
    def get_user_by_name(self, name):
        return self.dao.get_by_name(name)

    # Get user info by id
    def get_user_by_id(self, id):
        return self.dao.get_by_id(id)

    # Add user info
    def add_user(self, name, password):
        rc = self.dao.insert(name, password)
        self.dao.commit()
        return rc > 0