"""File with implementation of Treasure class."""
import turtle

class Treasure(turtle.Turtle):
    """A class to represent and print a treasure."""
    def __init__(self, x, y):
        """Constructs all the necessary attributes for the treasure object."""
        turtle.Turtle.__init__(self)
        self.shape("saphire.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        """Move object outside vidow size and hide it."""
        self.goto(5000, 5000)
        self.hideturtle()
