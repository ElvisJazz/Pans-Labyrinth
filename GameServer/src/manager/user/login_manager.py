# ======================================================================
# Function: Login
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from database.bl.user_info_bl import UserInfoBL
from database.dbcp_manager import DBCPManager
from message_from_client.register_login_mfc import RegisterAndLoginMessageFromClient
from info.user_info import UserInfo


class LoginManager(object):

    @classmethod
    def login(cls, login_mfc):
        conn = None
        try:
            if isinstance(login_mfc, RegisterAndLoginMessageFromClient):
                user_info = UserInfo()
                login_mfc.set_user_info(user_info)
                conn = DBCPManager.get_connection()
                user_info_bl = UserInfoBL(0, conn)
                db_user = user_info_bl.get_user_by_name(user_info.name)
                if db_user is None:
                    raise Exception("Username doesn't exist!")
                if db_user.password == user_info.password:
                    return db_user
                else:
                    raise Exception("Password wrong!")
            else:
                raise Exception("Instance of LoginMessageFromClient is expected!")
        except Exception, e:
            raise e
        finally:
            if conn is not None:
                conn.close()