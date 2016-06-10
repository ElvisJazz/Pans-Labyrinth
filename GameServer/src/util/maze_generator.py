# ======================================================================
# Function: Generate maze with recursive tree algorithm
# Author: Elvis Jia
# Date: 2016.6.8
# ======================================================================
import random


# Enum class of direction
class Direction:
    NULL=-1
    START=0
    RIGHT=1
    FRONT=2
    LEFT=3
    BACK=4

# Maze cell class
class MazeCell(object):
    def __init__(self):
        self.parent_pos = None
        self.is_visited = False
        self.is_enemy_spawner = False
        self.wall_right = False
        self.wall_front = False
        self.wall_left = False
        self.wall_back = False

# Class of target cell which is to be visited
class TargetCell(object):
    def __init__(self, row, column, move):
        self.row = row
        self.column = column
        self.move = move

class MazeGenerator(object):

    def __init__(self, rows, columns):
        self.rows =  abs(rows) if rows!=0 else 1
        self.columns = abs(columns) if columns!=0 else 1
        self.maze_array = [[MazeCell() for x in range(self.rows)] for y in range(self.columns)]
        self.target_cell_list = []

    def get_cell_in_range(self, max):
        return max

    def is_cell_in_target_list(self, row, column):
        for cell in self.target_cell_list:
            if cell.row == row and cell.column == column:
                return True
        return False

    def generate_maze(self):
        moves_available = [Direction.NULL for x in range(4)]
        moves_available_count = 0
        self.target_cell_list.append(TargetCell(random.randrange(0, self.rows), random.randrange(0, self.columns), Direction.START))
        # Generate walls if size of list is not 0
        while len(self.target_cell_list) > 0:
            moves_available_count = 0
            tc = self.target_cell_list[self.get_cell_in_range(len(self.target_cell_list)-1)]

            # Check move right
            if tc.column+1<self.columns and not self.maze_array[tc.row][tc.column+1].is_visited and not self.is_cell_in_target_list(tc.row, tc.column+1):
                moves_available[moves_available_count] = Direction.RIGHT
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].is_visited and tc.move != Direction.LEFT:
                self.maze_array[tc.row][tc.column].wall_right = True
                if tc.column+1 < self.columns:
                    self.maze_array[tc.row][tc.column+1].wall_left = True

            # Check move forward
            if tc.row+1<self.rows and not self.maze_array[tc.row+1][tc.column].is_visited and not self.is_cell_in_target_list(tc.row+1, tc.column):
                moves_available[moves_available_count] = Direction.FRONT
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].is_visited and tc.move != Direction.BACK:
                self.maze_array[tc.row][tc.column].wall_front = True
                if tc.row+1 < self.rows:
                    self.maze_array[tc.row+1][tc.column].wall_back = True

            # Check move left
            if tc.column>=1 and not self.maze_array[tc.row][tc.column-1].is_visited and not self.is_cell_in_target_list(tc.row, tc.column-1):
                moves_available[moves_available_count] = Direction.LEFT
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].is_visited and tc.move != Direction.RIGHT:
                self.maze_array[tc.row][tc.column].wall_left = True
                if tc.column >= 1:
                    self.maze_array[tc.row][tc.column-1].wall_right = True

            # Check move backward
            if tc.row >= 1 and not self.maze_array[tc.row-1][tc.column].is_visited and not self.is_cell_in_target_list(tc.row-1, tc.column):
                moves_available[moves_available_count] = Direction.BACK
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].is_visited and tc.move != Direction.FRONT:
                self.maze_array[tc.row][tc.column].wall_back = True
                if tc.row >= 1:
                    self.maze_array[tc.row-1][tc.column].wall_front = True

            # Check the enemy spawner
            if not self.maze_array[tc.row][tc.column].is_visited and moves_available_count == 0:
                self.maze_array[tc.row][tc.column].is_enemy_spawner = True

            # Set current cell visited
            self.maze_array[tc.row][tc.column].is_visited = True


            if moves_available_count > 0:
                random.seed()
                dir = moves_available[random.randrange(0, moves_available_count)]
                if dir == Direction.RIGHT:
                    self.target_cell_list.append(TargetCell(tc.row, tc.column+1, Direction.RIGHT))
                    self.maze_array[tc.row][tc.column+1].parent_pos = (tc.row, tc.column)
                elif dir == Direction.FRONT:
                    self.target_cell_list.append(TargetCell(tc.row+1, tc.column, Direction.FRONT))
                    self.maze_array[tc.row+1][tc.column].parent_pos = (tc.row, tc.column)
                elif dir == Direction.LEFT:
                    self.target_cell_list.append(TargetCell(tc.row, tc.column-1, Direction.LEFT))
                    self.maze_array[tc.row][tc.column-1].parent_pos = (tc.row, tc.column)
                elif dir == Direction.BACK:
                    self.target_cell_list.append(TargetCell(tc.row-1, tc.column, Direction.BACK))
                    self.maze_array[tc.row-1][tc.column].parent_pos = (tc.row, tc.column)
            else:
                self.target_cell_list.remove(tc)

        return self.maze_array
