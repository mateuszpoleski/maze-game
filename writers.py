"""File with implementation of StartWriter and EndWriter classes."""
import turtle
from constants import BLOCK_PIXEL_SIZE


class StartWriter(turtle.Turtle):
    """A class to write informations for the player at the start of the game."""
    def __init__(self, maze_size):
        turtle.Turtle.__init__(self)
        self.maze_border = ((maze_size - 1) // 2) * BLOCK_PIXEL_SIZE
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(-self.maze_border, self.maze_border+BLOCK_PIXEL_SIZE)


class EndWriter(turtle.Turtle):
    """A class to write informations for the player at the end of the game."""
    def __init__(self, maze_size):
        turtle.Turtle.__init__(self)
        self.maze_border = ((maze_size - 1) // 2) * BLOCK_PIXEL_SIZE
        self.color("red")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(-self.maze_border, -self.maze_border-(BLOCK_PIXEL_SIZE * 2))
