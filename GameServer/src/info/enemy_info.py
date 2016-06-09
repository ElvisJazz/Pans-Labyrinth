# ======================================================================
# Function: Store information of the enemy
# Date: 2016.5.27
# ======================================================================
from constant.enemy_action_type import EnemyActionType
from util.position import Position


class EnemyInfo(object):

    def __init__(self, enemy_id, enemy_type_id, health, max_health, position, hurt, experience, target_routine=(Position(0,0,0), Position(1,1,1)), action_type=EnemyActionType.RUN):
        self.enemy_id = enemy_id
        self.enemy_type_id = enemy_type_id
        self.health = health
        self.max_health = max_health
        self.position = position
        self.target_routine = target_routine
        self.hurt = hurt
        self.experience = experience
        self.action_type = action_type