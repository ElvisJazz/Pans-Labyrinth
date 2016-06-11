# ======================================================================
# Function: Message of the enemy which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from info.enemy_info import EnemyInfo


class EnemyMessageFromClient(object):

    def get_enemy_id(self):
        if hasattr(self, 'enemy_id'):
            return self.enemy_id
        else:
            return -1

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

    def set_enemy_list(self, enemy_dict):
        if isinstance(enemy_dict, dict):
            if hasattr(self, 'enemy_info_list'):
                enemy_info_list = self.enemy_info_list
                for enemy_info in enemy_info_list:
                    enemy = enemy_dict[enemy_info["enemy_id"]]
                    if enemy_info.has_key('health'):
                        enemy.health = enemy_info["health"]
                    if enemy_info.has_key('position'):
                        enemy.position = enemy_info["position"]
            else:
                raise Exception("Instance of List for enemy is expected!")
        else:
            raise Exception("Instance of Dict for enemy is expected!")