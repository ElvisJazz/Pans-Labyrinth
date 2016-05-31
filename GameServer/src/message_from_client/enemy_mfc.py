# ======================================================================
# Function: Message of the enemy which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from src.info.enemy_info import EnemyInfo


class EnemyMessageFromClient(object):

    def __init__(self):
        pass;

    def set_enemy_info(self, enemy_info):
        if isinstance(enemy_info, EnemyInfo):
            if hasattr(self, '_enemy_id'):
                enemy_info._enemy_id = self._enemy_id
            elif hasattr(self, '_health'):
                enemy_info._health = self._health
            elif hasattr(self, '_position'):
                enemy_info._position = self._position
        else:
            raise Exception("Instance of EnemyInfo is expected!")