import turtle


class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("walls.gif")
        self.penup()
        self.speed(0)
