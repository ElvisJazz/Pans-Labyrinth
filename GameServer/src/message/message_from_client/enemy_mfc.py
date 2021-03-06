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
            if hasattr(self,'next_position'):
                enemy_info.next_position = self.next_position
        else:
            raise Exception("Instance of EnemyInfo is expected!")

    def set_enemy_list(self, enemy_dict1, enemy_dict2):
        if isinstance(enemy_dict1, dict) and isinstance(enemy_dict2, dict):
            if hasattr(self, 'enemy_info_list'):
                enemy_info_list = self.enemy_info_list
                for enemy_info in enemy_info_list:
                    enemy = None
                    id = enemy_info["enemy_id"]
                    if enemy_dict1.has_key(id):
                        enemy = enemy_dict1[id]
                    else:
                        enemy = enemy_dict2[id]
                    if enemy_info.has_key('health'):
                        enemy.health = enemy_info["health"]
                    if enemy_info.has_key('position'):
                        enemy.position = enemy_info["position"]
                    if enemy_info.has_key('next_position'):
                        enemy.next_position = enemy_info["next_position"]
            else:
                raise Exception("Instance of List for enemy is expected!")
        else:
            raise Exception("Instance of Dict for enemy is expected!")