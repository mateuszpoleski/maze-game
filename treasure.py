import turtle


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("saphire.gif")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(5000, 5000)
        self.hideturtle()
