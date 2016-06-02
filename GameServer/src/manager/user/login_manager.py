# ======================================================================
# Function: Login
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from bl.user_info_bl import UserInfoBL
from message_from_client.login_mfc import LoginMessageFromClient
from user.user_info import UserInfo


class LoginManager(object):

    def __init__(self):
        pass

    def login(self, login_mfc):
        if isinstance(login_mfc, LoginMessageFromClient):
            user_info = UserInfo()
            login_mfc.set_user_info(user_info)
            db_user = UserInfoBL().get_user_by_name(user_info.name)
            if db_user.password == user_info.password:
                return db_user
            else:
                return None
        else:
            raise Exception("Instance of LoginMessageFromClient is expected!")