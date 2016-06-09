# ======================================================================
# Function: Manage the game for each player online
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from database.dbcp_manager import DBCPManager
from manager.game.enemy_manager import EnemyManager
from manager.game.player_manager import PlayerManager
from manager.game.scene_manager import SceneManager
from manager.game.weapon_manager import WeaponManager


class GameManager(object):

    def __init__(self, player_id):
        self.player_id = player_id
        self.is_running = True
        self.scene_manager = SceneManager(player_id)
        self.player_manager = PlayerManager(player_id)
        self.weapon_manager = WeaponManager(player_id)
        self.enemy_manager = EnemyManager(player_id, self)

    def load(self):
        self.scene_manager.load()
        self.player_manager.load()
        self.weapon_manager.load()
        self.enemy_manager.load()

    def save(self):
        flag = self.scene_manager.save()
        flag |= self.player_manager.save()
        flag |= self.weapon_manager.save()
        flag |= self.enemy_manager.save()
        conn = DBCPManager.get_connection(self.player_id)
        if flag:
            conn.commit()
        else:
            conn.rollback()
        return flag