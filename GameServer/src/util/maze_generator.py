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
        self.isVisited = False
        self.isEnemySpawner = False
        self.wallRight = False
        self.wallFront = False
        self.wallLeft = False
        self.wallBack = False

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
            if tc.column+1<self.columns and not self.maze_array[tc.row][tc.column+1].isVisited and not self.is_cell_in_target_list(tc.row, tc.column+1):
                moves_available[moves_available_count] = Direction.RIGHT
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].isVisited and tc.move != Direction.LEFT:
                self.maze_array[tc.row][tc.column].wallRight = True
                if tc.column+1 < self.columns:
                    self.maze_array[tc.row][tc.column+1].wallLeft = True

            # Check move forward
            if tc.row+1<self.rows and not self.maze_array[tc.row+1][tc.column].isVisited and not self.is_cell_in_target_list(tc.row+1, tc.column):
                moves_available[moves_available_count] = Direction.FRONT
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].isVisited and tc.move != Direction.BACK:
                self.maze_array[tc.row][tc.column].wallFront = True
                if tc.row+1 < self.rows:
                    self.maze_array[tc.row+1][tc.column].wallBack = True

            # Check move left
            if tc.column>=1 and not self.maze_array[tc.row][tc.column-1].isVisited and not self.is_cell_in_target_list(tc.row, tc.column-1):
                moves_available[moves_available_count] = Direction.LEFT
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].isVisited and tc.move != Direction.RIGHT:
                self.maze_array[tc.row][tc.column].wallLeft = True
                if tc.column >= 1:
                    self.maze_array[tc.row][tc.column-1].wallRight = True

            # Check move backward
            if tc.row >= 1 and not self.maze_array[tc.row-1][tc.column].isVisited and not self.is_cell_in_target_list(tc.row-1, tc.column):
                moves_available[moves_available_count] = Direction.BACK
                moves_available_count += 1
            elif not self.maze_array[tc.row][tc.column].isVisited and tc.move != Direction.FRONT:
                self.maze_array[tc.row][tc.column].wallBack = True
                if tc.row >= 1:
                    self.maze_array[tc.row-1][tc.column].wallFront = True

            # Check the enemy spawner
            if not self.maze_array[tc.row][tc.column].isVisited and moves_available_count == 0:
                self.maze_array[tc.row][tc.column].isEnemySpawner = True

            # Set current cell visited
            self.maze_array[tc.row][tc.column].isVisited = True

            if moves_available_count > 0:
                random.seed()
                dir = moves_available[random.randrange(0, moves_available_count)]
                if dir == Direction.RIGHT:
                    self.target_cell_list.append(TargetCell(tc.row, tc.column+1, Direction.RIGHT))
                elif dir == Direction.FRONT:
                    self.target_cell_list.append(TargetCell(tc.row+1, tc.column, Direction.FRONT))
                elif dir == Direction.LEFT:
                    self.target_cell_list.append(TargetCell(tc.row, tc.column-1, Direction.LEFT))
                elif dir == Direction.BACK:
                    self.target_cell_list.append(TargetCell(tc.row-1, tc.column, Direction.BACK))
            else:
                self.target_cell_list.remove(tc)

        return self.maze_array
