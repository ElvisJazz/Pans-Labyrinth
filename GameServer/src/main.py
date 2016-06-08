import json
from config.config_manager import ConfigManager
from constant.message_mark import MessageMark
from dispatcher import Dispatcher
import asyncore, socket
from util.maze_generator import MazeCell


class GameServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, int(port)))
        self.listen(10)

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            return
        (sock, addr) = pair
        print("incoming client: %s"%(repr(addr)))
        handler = GameHandler(sock)


class GameHandler(asyncore.dispatcher_with_send):

    def __init__(self, sock):
        asyncore.dispatcher_with_send.__init__(self, sock)
        self.message = ""

    def handle_read(self):
        data = self.recv(4096)
        if data is None:
            return
        elif data.endswith(MessageMark.END_MARK):
            self.message += data
            self.message = self.message[:-3]
            # Handle message
            Dispatcher.dispatch(self, self.message)
            self.message = ""
        else:
            self.message += data

    def handle_close(self):
        print("closed client: %s"% (repr(self.addr)))
        self.close()


def _input():
    while(True):
        data0 = raw_input()
        #client.send(data0)

ConfigManager.init()
(host, port) = "127.0.0.1", 6500 # sys.argv[2:];
server = GameServer(host, port)
asyncore.loop()



