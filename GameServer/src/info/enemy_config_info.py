# ======================================================================
# Function: Store information of the enemy config
# Date: 2016.5.31
# ======================================================================


class EnemyConfigInfo(object):

    def __init__(self, enemy_type, name, max_health, hurt, experience, amount):
        self.enemy_type = enemy_type
        self.name = name
        self.max_health = max_health
        self.amount = amount
        self.hurt = hurt
        self.experience = experience