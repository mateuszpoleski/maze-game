import random
from constants import BLOCK_PIXEL_SIZE


class Level:
    def __init__(self, MAZE_SIZE):
        self.maze = [['X' for x in range(MAZE_SIZE)] for y in range(MAZE_SIZE)]
        self.MAZE_SIZE = MAZE_SIZE

    def in_maze(self, i, j):
        return i >= 0 and i < self.MAZE_SIZE and j >= 0 and j < self.MAZE_SIZE

    def in_vizited(self, i, j, n):
        return i >= 0 and i < n and j >= 0 and j < n

    def give_dir(self, vizited, i, j):
        n = len(vizited)

        possible_dirs = []
        if self.in_vizited(i-1, j, n) and vizited[i-1][j] == 0:
            possible_dirs += ['N']
        if self.in_vizited(i+1, j, n) and vizited[i+1][j] == 0:
            possible_dirs += ['S']
        if self.in_vizited(i, j+1, n) and vizited[i][j+1] == 0:
            possible_dirs += ['E']
        if self.in_vizited(i, j-1, n) and vizited[i][j-1] == 0:
            possible_dirs += ['W']

        if len(possible_dirs) == 0:
            return 'Q'
        else:
            return random.choice(possible_dirs)

    def make_move(self, i, j, direction, vizited):
        if direction == 'N':
            self.maze[2*i][2*j + 1] = ' '
            i -= 1
            vizited[i][j] = 1
        elif direction == 'E':
            j += 1
            self.maze[2*i + 1][2*j] = ' '
            vizited[i][j] = 1
        if direction == 'S':
            i += 1
            self.maze[2*i][2*j + 1] = ' '
            vizited[i][j] = 1
        if direction == 'W':
            self.maze[2*i + 1][2*j] = ' '
            j -= 1
            vizited[i][j] = 1
        return i, j

    def print_maze(self):
        for row in self.maze:
            print(row)
        print()

    def create_guide_cells(self):
        for i, row in enumerate(self.maze):
            for j, _ in enumerate(row):
                if i % 2 == 1 and j % 2 == 1:
                    self.maze[i][j] = ' '

    def add_start(self):
        for i in range(self.MAZE_SIZE):
            if self.maze[i][1] == ' ':
                self.maze[i][0] = 'P'
                return

    def add_end(self):
        for i in reversed(range(self.MAZE_SIZE)):
            if self.maze[i][self.MAZE_SIZE-2] == ' ':
                self.maze[i][self.MAZE_SIZE-1] = 'E'
                return

    def add_treasures(self, prob=0.01):
        for i in range(self.MAZE_SIZE):
            for j in range(self.MAZE_SIZE):
                if i > 2 and self.maze[i][j] == ' ':
                    r = random.random()
                    if r < prob:
                        self.maze[i][j] = 'T'

    def create_maze(self):

        self.create_guide_cells()

        vizited = [[0 for x in range(self.MAZE_SIZE//2)]
                   for y in range(self.MAZE_SIZE//2)]
        vizited[0][0] = 1
        i, j = 0, 0

        vizited_stack = []
        vizited_stack.append((0, 0))

        while True:
            direction = self.give_dir(vizited, i, j)
            if direction == 'Q':
                i, j = vizited_stack.pop()
            else:
                vizited_stack.append((i, j))
                i, j = self.make_move(i, j, direction, vizited)
            if len(vizited_stack) == 0:
                break

    def create(self):
        self.create_maze()
        self.add_start()
        self.add_end()
        self.add_treasures()
