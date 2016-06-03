# ======================================================================
# Function: Dispatch messages to manager
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
from constant.message_mark import MessageMark
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from manager.game.game_manager import GameManager
from manager.manager_online import OnlineManager
from manager.user.login_manager import LoginManager
from manager.user.register_manager import RegisterManager
from message_from_client.base_message import BaseMessage
from util.message_packer import MessagePacker


class Dispatcher(object):

    @classmethod
    def dispatch(cls, socket, message):
        mfc = MessagePacker.pack(message)
        r_message = BaseMessage(mfc.message_type, mfc.target_type, mfc.sequence_id)
        reply = False
        # Dispatch message
        try:
            # Register
            if mfc.message_type == MessageType.REGISTER:
                reply = True
                r_message.success = RegisterManager.register(mfc)
            # Login
            elif mfc.message_type == MessageType.LOGIN:
                reply = True
                user_info = LoginManager.login(mfc)
                r_message.success = True if user_info is not None else False
                if r_message.success:
                    OnlineManager.add_game_manager(socket, user_info.player_id)
            # Update
            elif mfc.message_type == MessageType.UPDATE:
                game_manager = (OnlineManager.get_game_manager(socket))
                if mfc.target_type == MessageTargetType.PLAYER:
                    game_manager.player_manager.update(mfc)
                elif mfc.target_type == MessageTargetType.WEAPON:
                    game_manager.weapon_manager.update(mfc)
                elif mfc.target_type == MessageTargetType.ENEMY:
                    game_manager.enemy_manager.update(mfc)
            # Save
            elif mfc.message_type == MessageType.SAVE:
                reply = True
                r_message.success = OnlineManager.save_game_manager(socket)
            # Logout
            elif mfc.message_type == MessageType.LOGOUT:
                reply = True
                r_message.success = OnlineManager.remove_and_save_game_manager(socket)

        except Exception, e:
            r_message.message = str(e)
        # Send reply message
        if reply:
            cls.send(socket, r_message)

    @classmethod
    def send(cls, socket, r_message):
        json_str = MessagePacker.unpack(r_message)
        socket.send(json_str)


