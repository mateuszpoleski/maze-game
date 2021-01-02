"""File with implementation of Maze class."""
import turtle
import level
import player
import wall
import treasure
import writers
from constants import BLOCK_PIXEL_SIZE


class Maze:
    """A class to control flow of the game."""
    def __init__(self, maze_size):
        """
        Initializes everything that is needed to start a new game.

        maze_size -- Size in which maze will be created. Only odd sizes are possible.
        """
        self.treasures = {}
        self.level = level.Level(maze_size)
        self.player = player.Player(self.level, self.treasures, maze_size)
        self.start_writer = writers.StartWriter(maze_size)
        self.wall = wall.Wall()

        self.maze_size = maze_size

    def setup_maze(self):
        """Create graphical reprezentation of the maze."""
        maze_border = ((self.maze_size - 1) // 2) * BLOCK_PIXEL_SIZE
        for y_pos in range(self.maze_size):
            for x_pos in range(self.maze_size):
                character = self.level.maze[y_pos][x_pos]
                screen_x = -maze_border + (x_pos * BLOCK_PIXEL_SIZE)
                screen_y = maze_border - (y_pos * BLOCK_PIXEL_SIZE)

                if character == 'X':
                    self.wall.goto(screen_x, screen_y)
                    self.wall.stamp()

                if character == 'P':
                    self.player.goto(screen_x, screen_y)
                    self.player.pendown()

                if character == 'T':
                    self.treasures[(screen_x, screen_y)] = treasure.Treasure(
                        screen_x, screen_y)

    def start(self):
        """Start a new game."""
        self.start_writer.write(
            "R - restart  |  F - find path  |  E - exit", font=("Arial", 16, "normal"))
        self.level.create()
        self.setup_maze()
        turtle.Screen().onkey(self.reset, "r")
        turtle.Screen().onkey(self.reset, "y")

    def reset(self):
        """Reset game."""
        turtle.Screen().resetscreen()
        for turtl in turtle.Screen().turtles():
            turtl.hideturtle()
        game = Maze(self.maze_size)
        game.start()
