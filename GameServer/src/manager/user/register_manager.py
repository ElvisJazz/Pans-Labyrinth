# ======================================================================
# Function: Register
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from src.config.data_file_path import DataFilePath
from src.info.player_info import PlayerInfo
from src.manager.user.id_manager import IdManager
from src.message_from_client.register_mfc import RegisterMessageFromClient

try:
    import cPickle as pickle
except ImportError:
    import pickle

class RegisterManager(object):

    def __init__(self):
        """load the config information"""
        with open(DataFilePath.player_config_path, 'r') as f:
            self._player_info = pickle.load(f)
        with open(DataFilePath.weapon_config_path, 'r') as f:
            list = pickle.load(f)
            if len(list) > 0:
                self._weapon_info = list[0]

    def register(self, register_mfc):
        if isinstance(register_mfc, RegisterMessageFromClient):
            # Check whether the user has been existed

            play_info = PlayerInfo(IdManager.get_next_id(), self._player_info.health, self._player_info.max_health,
                self._player_info.experience, self._player_info.max_experience, self._player_info.weapon_list)

            # Store player information

            # Update id buffer
            IdManager.add_id(play_info.player_id)
        else:
            raise Exception("Instance of RegisterMessageFromClient is expected!")

