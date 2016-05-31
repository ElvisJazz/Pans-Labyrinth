# ======================================================================
# Function: Manage information of the enemy
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
try:
    import cPickle as pickle
except ImportError:
    import pickle

class EnemyManager(object):
    def __init__(self):
        self._enemy_list = []

    def save(self, path):
        """save the information of enemy"""
        with open(path, 'wb') as f:
            pickle.dump(self._enemy_list, f)

    def load(self, path):
        """load the information of enemy"""
        with open(path, 'rb') as f:
            self._enemy_list = pickle.load(f)