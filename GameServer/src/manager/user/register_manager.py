# ======================================================================
# Function: Register
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
import json
from database.bl.enemy_config_info_bl import EnemyConfigInfoBL
from database.bl.enemy_info_bl import EnemyInfoBL
from database.bl.maze_config_info_bl import MazeConfigInfoBL
from database.bl.maze_info_bl import MazeInfoBL
from database.bl.player_config_info_bl import PlayerConfigInfoBL
from database.bl.player_info_bl import PlayerInfoBL
from database.bl.user_info_bl import UserInfoBL
from database.bl.weapon_config_info_bl import WeaponConfigInfoBL
from database.bl.weapon_info_bl import WeaponInfoBL
from database.dbcp_manager import DBCPManager
from info.enemy_info import EnemyInfo
from info.maze_info import MazeInfo
from info.player_info import PlayerInfo
from info.weapon_info import WeaponInfo
from info.user_info import UserInfo
from message_from_client.system_mfc import SystemMessageFromClient
from util.maze_generator import MazeGenerator


class RegisterManager(object):

    @classmethod
    def register(cls, register_mfc):
        conn = None
        try:
            if isinstance(register_mfc, SystemMessageFromClient):
                user_info = UserInfo()
                register_mfc.set_user_info(user_info)
                conn = DBCPManager.get_connection()
                user_info_bl = UserInfoBL(0, conn)
                # Check whether the user has been existed
                if not user_info_bl.check_exist(user_info.name):
                    # Add user info to the db
                    if user_info_bl.add_user(user_info.name, user_info.password):
                        user_info = user_info_bl.get_user_by_name(user_info.name)
                        # Add game element of the user to db
                        flag = cls.add_player_info(user_info.player_id, conn) and cls.add_weapon_info(user_info.player_id, conn) and \
                               cls.add_enemy_info(user_info.player_id, conn) and cls.add_scene_info(user_info.player_id, conn)
                        if flag is False:
                            conn.rollback()
                            return False
                        else:
                            conn.commit()
                            return True
                    else:
                        conn.rollback()
                        return False
                else:
                    raise Exception("Username has existed!")
            else:
                raise Exception("Instance of RegisterMessageFromClient is expected!")
        except Exception, e:
            conn.rollback()
            raise e
        finally:
            if conn is not None:
                conn.close()

    @classmethod
    def add_player_info(cls, player_id, conn):
        # Get player config
        player_config_bl = PlayerConfigInfoBL(player_id)
        player_config_bl.set_conn(conn)
        player_config = player_config_bl.get_by_id(0)
        # Create player info record
        player_info = PlayerInfo(player_id, player_config.type_id, player_config.level, (0,0,0), player_config.max_health,
                                 player_config.max_health, 0, player_config.max_experience, 0)
        player_info_bl = PlayerInfoBL(player_id)
        player_info_bl.set_conn(conn)
        return player_info_bl.add_player(player_info)

    @classmethod
    def add_weapon_info(cls, player_id, conn):
        # Get weapon config
        weapon_config_bl = WeaponConfigInfoBL(player_id)
        weapon_config_bl.set_conn(conn)
        weapon_config_list = weapon_config_bl.get_list()
        # Create weapon list according to config list
        weapon_list = []
        for config in weapon_config_list:
            weapon = WeaponInfo(0, config.type_id, config.weapon_type, False, config.max_bullets_in_gun, config.max_bullets_in_bag,
                                config.max_bullets_in_gun, config.max_bullets_in_bag,(0,0,0), config.hurt, config.default)
            weapon_list.append(weapon)
        weapon_info_bl = WeaponInfoBL(player_id, conn)
        return weapon_info_bl.add_list(weapon_list)

    @classmethod
    def add_enemy_info(cls, player_id, conn):
        # Get enemy config
        # enemy_config_bl = EnemyConfigInfoBL(player_id)
        # enemy_config_bl.set_conn(conn)
        # enemy_config_list = enemy_config_bl.get_list()
        # # Create enemy list according to config list
        # enemy_list = []
        # id = 0
        # for config in enemy_config_list:
        #     for i in range(config.amount):
        #         enemy = EnemyInfo(id, config.type_id, config.max_health, config.max_health, (0,0,0), config.hurt, config.experience)
        #         enemy_list.append(enemy)
        #         id += 1
        # enemy_info_bl = EnemyInfoBL(player_id)
        # enemy_info_bl.set_conn(conn)
        # return enemy_info_bl.add_list(enemy_list)
        return True

    @classmethod
    def add_scene_info(cls, player_id, conn):
        # Get maze config
        maze_config_bl = MazeConfigInfoBL(player_id)
        maze_config_bl.set_conn(conn)
        maze_config_list = maze_config_bl.get_list()
        # Create maze and save record
        for config in maze_config_list:
            if config.default == 1:
                tmp_array = MazeGenerator(config.row, config.column).generate_maze()
                maze_array = []
                for i in range(0, config.row):
                    for j in range(0, config.column):
                        maze_array.append(tmp_array[i][j])
                maze_json = json.dumps(maze_array, default=lambda obj: obj.__dict__)
                maze = MazeInfo(0, config.type_id, config.row, config.column, maze_json, config.width, config.height)
                maze_info_bl = MazeInfoBL(player_id)
                maze_info_bl.set_conn(conn)
                return maze_info_bl.add_maze(maze)