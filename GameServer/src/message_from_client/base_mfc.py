# ======================================================================
# Function: Message base class
# Author: Elvis Jia
# Date: 2016.6.27
# ======================================================================


class BaseMessageFromClient(object):

    def __init__(self):
        self.message_type = ""
        self.target_type = ""
