# ======================================================================
# Function: Store information of the player
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================


class PlayerInfo(object):

    def __init__(self, player_id, type_id, level, position, health, max_health, experience, max_experience, dead_num):
        self.player_id = player_id
        self.type_id = type_id
        self.level = level
        self.position = position
        self.health = health
        self.max_health = max_health
        self.experience = experience
        self.max_experience = max_experience
        self.dead_num = dead_num
