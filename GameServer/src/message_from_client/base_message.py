# ======================================================================
# Function: Message base class
# Author: Elvis Jia
# Date: 2016.6.27
# ======================================================================


class BaseMessage(object):

    def __init__(self, message_type="", target_type="", sequence_id=0):
        self.message_type = message_type
        self.target_type = target_type
        self.sequence_id = sequence_id
        self.message = ""
        self.success = False
