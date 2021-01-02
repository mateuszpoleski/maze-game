from constants import BLOCK_PIXEL_SIZE
import turtle


class StartWriter(turtle.Turtle):
    def __init__(self, MAZE_SIZE):
        turtle.Turtle.__init__(self)
        self.MAZE_BORDER = ((MAZE_SIZE - 1) // 2) * BLOCK_PIXEL_SIZE
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(-self.MAZE_BORDER, self.MAZE_BORDER+BLOCK_PIXEL_SIZE)


class EndWriter(turtle.Turtle):
    def __init__(self, MAZE_SIZE):
        turtle.Turtle.__init__(self)
        self.MAZE_BORDER = ((MAZE_SIZE - 1) // 2) * BLOCK_PIXEL_SIZE
        self.color("red")
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(-self.MAZE_BORDER, -self.MAZE_BORDER-(BLOCK_PIXEL_SIZE * 2))
