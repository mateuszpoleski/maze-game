"""File with implementation of Wall class."""
import turtle


class Wall(turtle.Turtle):
    """A class to draw borders of the maze."""
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("walls.gif")
        self.penup()
        self.speed(0)
