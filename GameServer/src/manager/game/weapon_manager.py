# ======================================================================
# Function: Manage information of the weapon
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
try:
    import cPickle as pickle
except ImportError:
    import pickle

class WeaponManager(object):
    def __init__(self):
        self._weapon_list = []

    def save(self, path):
        """save the information of enemy"""
        with open(path, 'wb') as f:
            pickle.dump(self._weapon_list, f)

    def load(self, path):
        """load the information of enemy"""
        with open(path, 'rb') as f:
            self._weapon_list = pickle.load(f)