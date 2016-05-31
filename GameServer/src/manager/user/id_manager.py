# ======================================================================
# Function: Id manager
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================
from src.config.data_file_path import DataFilePath

try:
    import cPickle as pickle
except ImportError:
    import pickle


class IdManager(object):

    Id_list = []

    @classmethod
    def load(cls):
        """load the id list"""
        with open(DataFilePath.id_file_path, 'rb') as f:
            cls.Id_list = pickle.load(f)

    @classmethod
    def save(cls):
        """save the id list"""
        with open(DataFilePath.id_file_path, 'wb') as f:
            pickle.dump(cls.Id_list, f)

    @classmethod
    def get_next_id(cls):
        if len(cls.Id_list) > 0:
            cls.Id_list.sort(reverse=True)
            return cls.Id_list[0]+1
        else:
            return 0

    @classmethod
    def add_id(cls, id):
        cls.Id_list.insert(0, id)
        cls.save()