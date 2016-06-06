# ======================================================================
# Function: Store information of the scene
# Author: Elvis Jia
# Date: 2016.5.28
# ======================================================================


class SceneInfo(object):

    def __init__(self, width):
        self.width = width

    def generate_maze(self):
        pass

    def get_index_pos(self, real_pos):
        """ Get simplified index position according to real position """
        return real_pos[0]/self.width+1, 0, real_pos[2]/self.width+1

    def get_real_pos(self, index_pos):
        """ Get real position according to simplified index position """
        return (index_pos[0]-1)*self.width(), 0, (index_pos[2]-1)*self.width+1
