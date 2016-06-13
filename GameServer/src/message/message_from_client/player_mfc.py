# ======================================================================
# Function: Message of the player which is from client
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from database.bl.player_config_info_bl import PlayerConfigInfoBL
from database.bl.player_info_bl import PlayerInfoBL
from info.player_info import PlayerInfo


class PlayerMessageFromClient(object):

    def set_player_info(self, player_info):
        has_reply = False
        if isinstance(player_info, PlayerInfo):
            # if hasattr(self, 'player_id'):
            #     player_info.player_id = self.player_id
            #
            if hasattr(self, 'position'):
                player_info.position = self.position
            if hasattr(self, 'health'):
                player_info.health = self.health
            if hasattr(self, 'experience'):
                if self.experience > player_info.max_experience:
                    player_info.experience -= player_info.max_experience
                    player_info.type_id += 1
                    # Get player config
                    player_config_bl = PlayerConfigInfoBL(player_info.player_id, None, True)
                    player_config = player_config_bl.get_by_id(player_info.type_id)
                    player_info.max_experience = player_config.max_experience
                    player_info.level = player_config.level
                    has_reply = True
                else:
                    player_info.experience = self.experience
            if hasattr(self, 'dead_num'):
                player_info.dead_num = self.dead_num

            return has_reply
        else:
            raise Exception("Instance of PlayerInfo is expected!")