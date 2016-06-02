# ======================================================================
# Function: Store information of the weapon
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================

try:
    import cPickle as pickle
except ImportError:
    import pickle


class WeaponInfo(object):

    def __init__(self, weapon_id, weapon_type_id, take, current_bullets_in_gun, current_bullets_in_bag, max_bullets_in_gun,
                 max_bullets_in_bag, weapon_position, hurt):
        self.weapon_id = weapon_id
        self.weapon_type_id = weapon_type_id
        self.weapon_position = weapon_position
        self.take = take
        self.current_bullets_in_gun = current_bullets_in_gun
        self.current_bullets_in_bag = current_bullets_in_bag
        self.max_bullets_in_gun = max_bullets_in_gun
        self.max_bullets_in_bag = max_bullets_in_bag
        self.hurt = hurt
