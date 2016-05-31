# ======================================================================
# Function: Store information of the weapon config
# Date: 2016.5.31
# ======================================================================


class WeaponConfigInfo(object):

    def __init__(self, type_id, weapon_type,  max_bullets_in_gun, max_bullets_in_bag, hurt, amount):
        self.type_id = type_id
        self.weapon_type = weapon_type
        self.max_bullets_in_gun = max_bullets_in_gun
        self.max_bullets_in_bag = max_bullets_in_bag
        self.hurt = hurt
        self.amount = amount