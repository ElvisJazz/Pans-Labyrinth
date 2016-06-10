# ======================================================================
# Function: Store information of the maze config
# Date: 2016.5.31
# ======================================================================


class MazeConfigInfo(object):

    def __init__(self, type_id, row, column, width, height, default):
        self.type_id = type_id
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.default = default