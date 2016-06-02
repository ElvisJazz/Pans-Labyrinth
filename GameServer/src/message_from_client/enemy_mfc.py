# ======================================================================
# Function: Message of the enemy which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.enemy_info import EnemyInfo


class EnemyMessageFromClient(object):

    def __init__(self):
        pass;

    def set_enemy_info(self, enemy_info):
        if isinstance(enemy_info, EnemyInfo):
            if hasattr(self, 'enemy_id'):
                enemy_info.enemy_id = self.enemy_id
            if hasattr(self, 'health'):
                enemy_info.health = self.health
            if hasattr(self, 'position'):
                enemy_info.position = self.position
        else:
            raise Exception("Instance of EnemyInfo is expected!")