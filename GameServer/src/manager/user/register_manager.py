# ======================================================================
# Function: Register
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from src.bl.enemy_config_info_bl import EnemyConfigInfoBL
from src.bl.enemy_info_bl import EnemyInfoBL
from src.bl.player_config_info_bl import PlayerConfigInfoBL
from src.bl.player_info_bl import PlayerInfoBL
from src.bl.user_info_bl import UserInfoBL
from src.bl.weapon_config_info_bl import WeaponConfigInfoBL
from src.bl.weapon_info_bl import WeaponInfoBL
from src.database.dbcp_manager import DBCPManager
from src.info.enemy_info import EnemyInfo
from src.info.player_info import PlayerInfo
from src.info.weapon_info import WeaponInfo
from src.message_from_client.register_mfc import RegisterMessageFromClient
from src.user.user_info import UserInfo

class RegisterManager(object):

    def __init__(self):
        pass

    def register(self, register_mfc):
        if isinstance(register_mfc, RegisterMessageFromClient):
            user_info = UserInfo()
            register_mfc.set_enemy_info(user_info)
            user_info_bl = UserInfoBL()
            # Check whether the user has been existed
            if user_info_bl.check_exist(user_info.name):
                # Add user info to the db
                if user_info_bl.add_user(user_info.name, user_info.password):
                    user_info = user_info_bl.get_user_by_name(user_info.name)
                    # Add game element of the user to db
                    flag = self.add_player_info(user_info.player_id) and self.add_weapon_info(user_info.player_id) and \
                           self.add_enemy_info(user_info.player_id) and self.add_scene_info(user_info.player_id)
                    conn = DBCPManager.get_connection(user_info.player_id)
                    if flag is False:
                        user_info_bl.rollback()
                        conn.rollback()
                        return False
                    else:
                        user_info_bl.commit()
                        conn.commit()
                        return True
                else:
                    user_info_bl.rollback()
                    return False
            else:
                raise Exception("Username has existed!")
        else:
            raise Exception("Instance of RegisterMessageFromClient is expected!")

    def add_player_info(self, player_id):
        # Get player config
        player_config_bl = PlayerConfigInfoBL(player_id)
        player_config = player_config_bl.get_by_id(player_id)
        # Create player info record
        player_info = PlayerInfo(player_id, player_config.type_id, player_config.level, (0,0,0), player_config.max_health,
                                 player_config.max_health, player_config.max_experience, player_config.max_experience, [])
        player_info_bl = PlayerInfoBL(player_id)
        return player_info_bl.add_player(player_info)

    def add_weapon_info(self, player_id):
        # Get weapon config
        weapon_config_bl = WeaponConfigInfoBL(player_id)
        weapon_config_list = weapon_config_bl.get_list()
        # Create weapon list according to config list
        weapon_list = []
        for config in weapon_config_list:
            weapon = WeaponInfo(0, config.type_id,False, config.max_bullets_in_gun, config.max_bullets_in_bag,
                                config.max_bullets_in_gun, config.max_bullets_in_bag,(0,0,0), config.hurt)
            weapon_list.append(weapon)
        weapon_info_bl = WeaponInfoBL(player_id)
        return weapon_info_bl.add_list(weapon_list)

    def add_enemy_info(self, player_id):
        # Get enemy config
        enemy_config_bl = EnemyConfigInfoBL(player_id)
        enemy_config_list = enemy_config_bl.get_list()
        # Create enemy list according to config list
        enemy_list = []
        for config in enemy_config_list:
            enemy = EnemyInfo(0, config.enemy_type, config.max_health, config.max_health, (0,0,0), config.hurt, config.experience)
            enemy_list.append(enemy)
        enemy_info_bl = EnemyInfoBL(player_id)
        return enemy_info_bl.add_list(enemy_info_bl)

    def add_scene_info(self, player_id):
        return True