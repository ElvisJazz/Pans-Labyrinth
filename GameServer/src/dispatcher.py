# ======================================================================
# Function: Dispatch messages to manager
# Author: Elvis Jia
# Date: 2016.5.27
# ======================================================================
import traceback
from constant.message_target_type import MessageTargetType
from constant.message_type import MessageType
from manager.manager_online import OnlineManager
from manager.user.login_manager import LoginManager
from manager.user.register_manager import RegisterManager
from message_to_client.register_login_mtc import RegisterAndLoginMessage
from util.message_packer import MessagePacker


class Dispatcher(object):

    @classmethod
    def dispatch(cls, socket, message):
        mfc = MessagePacker.pack(message)
        reply = False
        r_message = None
        # Dispatch message
        try:
            # Register
            if mfc.message_type == MessageType.REGISTER:
                reply = True
                r_message = RegisterAndLoginMessage(mfc.message_type, mfc.target_type, mfc.sequence_id)
                r_message.success = RegisterManager.register(mfc)

            # Login
            elif mfc.message_type == MessageType.LOGIN:
                reply = True
                r_message = RegisterAndLoginMessage(mfc.message_type, mfc.target_type, mfc.sequence_id)
                user_info = LoginManager.login(mfc)
                r_message.success = True if user_info is not None else False
                if r_message.success:
                    if OnlineManager.has_manager(user_info.player_id):
                        OnlineManager.update_socket(user_info.player_id, socket)
                    else:
                        OnlineManager.add_game_manager(socket, user_info.player_id)
                    game_manager = OnlineManager.get_game_manager(socket)
                    game_manager.is_running = True
                    # Recover last scene
                    game_manager.weapon_manager.generate_default_weapon()
                    game_manager.scene_manager.generate()
                    game_manager.player_manager.generate()
                    game_manager.enemy_manager.generate()
                    # Start generating new enemies in fixed time
                    game_manager.enemy_manager.generate_in_time()

            # Update
            elif mfc.message_type == MessageType.UPDATE:
                game_manager = (OnlineManager.get_game_manager(socket))
                if game_manager is None:
                    raise "Please login!"
                if mfc.target_type == MessageTargetType.PLAYER:
                    game_manager.player_manager.update(mfc)
                    game_manager.enemy_manager.update_client_enemy()
                elif mfc.target_type == MessageTargetType.WEAPON:
                    game_manager.weapon_manager.update(mfc)
                elif mfc.target_type == MessageTargetType.ENEMY:
                    game_manager.enemy_manager.update(mfc)

            # Save
            elif mfc.message_type == MessageType.SAVE:
                reply = True
                #r_message.success = OnlineManager.save_game_manager(socket)

            # Logout
            elif mfc.message_type == MessageType.LOGOUT:
                reply = True
                #r_message.success = OnlineManager.remove_and_save_game_manager(socket)

        except Exception, e:
            if r_message is not None:
                r_message.message = str(e)
            traceback.print_exc()
        # Send reply message
        if reply and r_message is not None:
            cls.send(socket, r_message)

    @classmethod
    def send(cls, socket, r_message):
        if not socket.connected:
            game_manager = OnlineManager.get_game_manager(socket)
            game_manager.is_running = False
        else:
            json_str = MessagePacker.unpack(r_message)
            socket.send(json_str)



