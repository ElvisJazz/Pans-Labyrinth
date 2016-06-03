# ======================================================================
# Function: Manage all other managers of game online
# Author: Elvis Jia
# Date: 2016.6.3
# ======================================================================
from database.dbcp_manager import DBCPManager
from manager.game.game_manager import GameManager


class OnlineManager(object):

    # socket->key, GameManager object->value
    manager_buffer = {}

    @classmethod
    def add_game_manager(cls, socket, player_id):
        """Create and add new game manager"""
        if cls.manager_buffer.has_key(socket):
            return
        else:
            game_manager = GameManager(player_id)
            game_manager.load()
            cls.manager_buffer[socket] = game_manager

    @classmethod
    def remove_and_save_game_manager(cls, socket, save=False):
        """Remove the game manager when the player offline"""
        if cls.manager_buffer.has_key(socket):
            game_manager = cls.manager_buffer[socket]
            if save and not game_manager.save():
                raise Exception("Failed to save game data. Please try again!")
            # remove socket from DBCPManager
            DBCPManager.close_conn(game_manager.player_id)
            return True;

    @classmethod
    def get_game_manager(cls, socket):
        if cls.manager_buffer.has_key(socket):
            return cls.manager_buffer[socket]
        else:
            return None

    @classmethod
    def save_game_manager(cls, socket):
        if cls.manager_buffer.has_key(socket):
            if not cls.manager_buffer[socket].save():
                raise Exception("Failed to save game data. Please try again!")
            return True