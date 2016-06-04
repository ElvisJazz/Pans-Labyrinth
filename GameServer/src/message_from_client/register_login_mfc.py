# ======================================================================
# Function: Message of the register or login which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.user_info import UserInfo


class RegisterAndLoginMessageFromClient(object):

    def set_user_info(self, user_info):
        if isinstance(user_info, UserInfo):
            if hasattr(self, 'name'):
                user_info.name = self.name
            if hasattr(self, 'password'):
                user_info.password = self.password
        else:
            raise Exception("Instance of UserInfo is expected!")