from src.config.config_manager import ConfigManager
from src.dao.user_info_dao import UserInfoDao
from src.database.dbcp_manager import DBCPManager

__author__ = 'ElvisJia'

import sys,os,time;
import asyncore,socket;
import thread;

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
        self.send("winlin");
        time.sleep(3);
        self.send(data);


def _input():
    while(True):
        data0 = raw_input();
        #client.send(data0)

#
# mode = "client";
# if mode == "client":
#     (host, port, path) = "127.0.0.1", 6500, "fd";  #sys.argv[2:];
#     client = HTTPClient(host, port, path);
#     thread.start_new_thread(_input,());
#     asyncore.loop();
# else:
#     (host, port) = "127.0.0.1", 6500; # sys.argv[2:];
#     server = EchoServer(host, port);
#     asyncore.loop();

ConfigManager.init()
DBCPManager.init()
u = UserInfoDao()
l = u.insert('hh23', '123')
print(l)