# ======================================================================
# Function: Manage information of the scene for scene
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
try:
    import cPickle as pickle
except ImportError:
    import pickle

class SceneManager(object):
    def __init__(self):
        self._scene_info = None

    def save(self, path):
        """save the information of scene"""
        with open(path, 'wb') as f:
            pickle.dump(self._scene_info, f)

    def load(self, path):
        """load the information of scene"""
        with open(path, 'rb') as f:
            self._scene_info = pickle.load(f)