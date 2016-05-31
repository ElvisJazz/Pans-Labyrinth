# ======================================================================
# Function: Store information of the player config
# Author: Elvis Jia
# Date: 2016.5.31
# ======================================================================

class PlayerConfigInfo(object):

    def __init__(self, type_id, max_health, max_experience, level):
        self.type_id = type_id
        self.level = level
        self.max_health = max_health
        self.max_experience = max_experience