# ======================================================================
# Function: Pack and unpack message
# Author: Elvis Jia
# Date: 2016.6.3
# ======================================================================
import json

from constant.message_mark import MessageMark
from message_from_client.enemy_mfc import EnemyMessageFromClient
from message_from_client.player_mfc import PlayerMessageFromClient
from message_from_client.system_mfc import SystemMessageFromClient
from message_from_client.weapon_mfc import WeaponMessageFromClient
from constant.message_target_type import MessageTargetType


class MessagePacker(object):

    @classmethod
    def pack(cls, json_str):
        dic = json.loads(json_str)
        mfc = None
        # System message from client
        if dic['target_type'] == MessageTargetType.SYSTEM:
            mfc = SystemMessageFromClient()
        # Player message from client
        elif dic['target_type'] == MessageTargetType.PLAYER:
            mfc = PlayerMessageFromClient()
        # Enemy message from client
        elif dic['target_type'] == MessageTargetType.ENEMY:
            mfc = EnemyMessageFromClient()
        # Weapon message from client
        elif dic['target_type'] == MessageTargetType.WEAPON:
            mfc = WeaponMessageFromClient()
        mfc.__dict__.update(dic)
        return mfc

    @classmethod
    def unpack(cls, message):
        json_str = json.dumps(message, default=lambda obj: obj.__dict__)
        json_str += MessageMark.END_MARK
        return json_str