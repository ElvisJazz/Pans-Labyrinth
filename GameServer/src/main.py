import sqlite3
from database.dbcp_manager import DBCPManager
from manager.user.register_manager import RegisterManager
from message_from_client.register_mfc import RegisterMessageFromClient
from config.config_manager import ConfigManager

__author__ = 'ElvisJia'

import time;
import asyncore,socket;


class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self);
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM);
        self.set_reuse_addr();
        self.bind((host, int(port)));
        self.listen(10);

    def handle_accept(self):
        pair = self.accept();
        if pair is None:
            return;
        (sock, addr) = pair;
        print("incoming client: %s"%(repr(addr)));
        handler = EchoHandler(sock);


class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192);
        if data is None:
            return;
        self.send("abcdefghijeklmnopqrstuvwxyz");
        time.sleep(3);
        self.send(data);

    def handle_close(self):
        print("closed client: %s"%(repr(self.addr)));
        self.close()


def _input():
    while(True):
        data0 = raw_input();
        #client.send(data0)



(host, port) = "127.0.0.1", 6500; # sys.argv[2:];
server = EchoServer(host, port)
asyncore.loop()


