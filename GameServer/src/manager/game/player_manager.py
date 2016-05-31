# ======================================================================
# Function: Manage information of the player online
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
try:
    import cPickle as pickle
except ImportError:
    import pickle


class PlayerManager(object):
    def __init__(self):
        self._player_info = None

    def save(self, path):
        """save the information of player"""
        with open(path, 'wb') as f:
            pickle.dump(self._player_info, f)

    def load(self, path):
        """load the information of player"""
        with open(path, 'rb') as f:
            self._player_info = pickle.load(f)