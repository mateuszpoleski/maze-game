"""File with implementation of Level class."""
import random
import utl

class Level:
    """
    A class to represent a level of the     game.
    Generates random maze, treasures, end points etc.
    """
    def __init__(self, maze_size):
        """Constructs 2D array reprezentation of maze filled with 'X'"""
        self.maze = [['X' for x in range(maze_size)] for y in range(maze_size)]
        self.maze_size = maze_size

    def in_maze(self, i, j):
        """Return if given coords are insade a maze."""
        return 0 <= i < self.maze_size and 0 <= j < self.maze_size

    @staticmethod
    def give_dir(vizited, i, j):
        """
        Gives a random position in which we can move while creating maze.
        If none are possible returns 'Q'.
        """
        vizited_size = len(vizited)

        possible_dirs = []
        if utl.in_range(i-1, j, vizited_size) and vizited[i-1][j] == 0:
            possible_dirs += ['N']
        if utl.in_range(i+1, j, vizited_size) and vizited[i+1][j] == 0:
            possible_dirs += ['S']
        if utl.in_range(i, j+1, vizited_size) and vizited[i][j+1] == 0:
            possible_dirs += ['E']
        if utl.in_range(i, j-1, vizited_size) and vizited[i][j-1] == 0:
            possible_dirs += ['W']

        if len(possible_dirs) == 0:
            return 'Q'
        return random.choice(possible_dirs)

    def make_move(self, i, j, direction, vizited):
        """
        Given a direction makes a move and creates empty space in a maze for that place.
        After that returns current coords in a maze.
        """
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
        """Print maze in a more human redable format. Used for debug only."""
        for row in self.maze:
            print(row)
        print()

    def create_guide_cells(self):
        """
        Creates guide cells in a maze.
        They ale leter used in the algorithm for generating random maze.
        """
        for i, row in enumerate(self.maze):
            for j, _ in enumerate(row):
                if i % 2 == 1 and j % 2 == 1:
                    self.maze[i][j] = ' '

    def add_start(self):
        """Add start point to the already generated maze."""
        for i in range(self.maze_size):
            if self.maze[i][1] == ' ':
                self.maze[i][0] = 'P'
                return

    def add_end(self):
        """Add end point to the already generated maze."""
        for i in reversed(range(self.maze_size)):
            if self.maze[i][self.maze_size-2] == ' ':
                self.maze[i][self.maze_size-1] = 'E'
                return

    def add_treasures(self, prob=0.01):
        """
        Add treasures to the already generated maze.

        prob -- probability that on given empty position in the maze treasure will be created.
        """
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                if i > 2 and self.maze[i][j] == ' ':
                    rand = random.random()
                    if rand < prob:
                        self.maze[i][j] = 'T'

    def create_maze(self):
        """Create random maze."""
        self.create_guide_cells()

        vizited = [[0 for x in range(self.maze_size//2)]
                   for y in range(self.maze_size//2)]
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
        """Create random maze with all needed features."""
        self.create_maze()
        self.add_start()
        self.add_end()
        self.add_treasures()
