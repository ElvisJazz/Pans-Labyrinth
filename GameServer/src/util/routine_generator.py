# ======================================================================
# Function: Generate routine of maze for enemy
# Author: Elvis Jia
# Date: 2016.6.10
# ======================================================================


class RoutineGenerator(object):

    def __init__(self, maze_array):
        self._maze_array = maze_array

    def get_routine(self, start_index_pos, target_index_pos):
        """
        get routine from start position to target position
        :param start_index_pos:
        :param target_iondex_pos:
        :return: position of routine list
        """
        if self.check_pos_equal(start_index_pos, target_index_pos):
            return []
        routine_to_start = self.find_root_routine(start_index_pos)
        routine_to_target = self.find_root_routine(target_index_pos)
        common_root = None
        # visit each node from root to cross node
        while len(routine_to_start) > 0 and len(routine_to_target) > 0 and self.check_pos_equal(routine_to_start[0], routine_to_target[0]):
            routine_to_start.pop(0)
            common_root = routine_to_target.pop(0)
        # merge routine
        routine_to_start.reverse()
        if len(routine_to_start) == 0 or len(routine_to_target) == 0 or ((common_root[0] != routine_to_start[-1][0] or common_root[0] != routine_to_target[0][0]) and \
                (common_root[1] != routine_to_start[-1][1] or common_root[1] != routine_to_target[0][1])):
            routine_to_start.append(common_root)
        routine_to_start.extend(routine_to_target)
        return routine_to_start

    def find_root_routine(self, pos):
        routine_list = [(pos[1], pos[0])]
        is_row_same = False
        is_col_same = False
        parent = self._maze_array[pos[1]][pos[0]]["parent_pos"]
        while parent is not None:
            # simplify the routine by combine nodes in a line
            if parent[0] == routine_list[0][0]:
                if is_row_same:
                    routine_list.pop(0)
                else:
                    is_row_same = True
                    is_col_same = False
            elif parent[1] == routine_list[0][1]:
                if is_col_same:
                    routine_list.pop(0)
                else:
                    is_row_same = False
                    is_col_same = True
            routine_list.insert(0, parent)
            parent = self._maze_array[parent[0]][parent[1]]["parent_pos"]
        return routine_list

    def check_pos_equal(self, pos1, pos2):
         return pos1[0] == pos2[0] and pos1[1] == pos2[1]
