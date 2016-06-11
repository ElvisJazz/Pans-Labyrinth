# ======================================================================
# Function: Store information of the enemy config
# Date: 2016.5.31
# ======================================================================


class EnemyConfigInfo(object):

    def __init__(self, type_id, enemy_type, max_health, hurt, experience, amount, distance):
        self.enemy_type = enemy_type
        self.type_id = type_id
        self.max_health = max_health
        self.amount = amount
        self.hurt = hurt
        self.experience = experience
        self.attack_distance = distance