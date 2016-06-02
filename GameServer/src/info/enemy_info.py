# ======================================================================
# Function: Store information of the enemy
# Date: 2016.5.27
# ======================================================================


class EnemyInfo(object):

    def __init__(self, enemy_id, enemy_type_id, health, max_health, position, hurt, experience, target_position=(0,0,0)):
        self.enemy_id = enemy_id
        self.enemy_type_id = enemy_type_id
        self.health = health
        self.max_health = max_health
        self.position = position
        self.target_position = target_position
        self.hurt = hurt
        self.experience = experience