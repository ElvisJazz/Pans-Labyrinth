# ======================================================================
# Function: Store information of the player
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================


class PlayerInfo(object):

    def __init__(self, id, type_id, level, position, health, max_health, experience, max_experience, weapon_list=[]):
        self.player_id = id
        self.type_id = type_id
        self.level = level
        self.position = position
        self.health = health
        self.max_health = max_health
        self.experience = experience
        self.max_experience = max_experience
        if isinstance(weapon_list, list):
            self.weapon_list = weapon_list
        else:
            self.weapon_list = []
