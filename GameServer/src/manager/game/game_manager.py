# ======================================================================
# Function: Manage the game for each player online
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from manager.game.enemy_manager import EnemyManager
from manager.game.player_manager import PlayerManager
from manager.game.scene_manager import SceneManager


class GameManager(object):

    def __init__(self, player_id):
        self._player_id = player_id
        self._scene_manager = SceneManager()
        self._player_manager = PlayerManager()
        self._enemy_manager = EnemyManager()

    def load(self):
        self._scene_manager.load(DirectoryPath.base_scene_file_path+self._player_id);
        self._player_manager.load(DirectoryPath.base_player_file_path+self._player_id);
        self._enemy_manager.load(DirectoryPath.base_enemy_file_path+self._player_id);

    def save(self):
        self._scene_manager.save(DirectoryPath.base_scene_file_path+self._player_id);
        self._player_manager.save(DirectoryPath.base_player_file_path+self._player_id);
        self._enemy_manager.save(DirectoryPath.base_enemy_file_path+self._player_id);