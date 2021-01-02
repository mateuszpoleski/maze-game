from constants import BLOCK_PIXEL_SIZE
import copy

import utl
import turtle
import writers


class Player(turtle.Turtle):
    """A class to represent a player of the game."""

    def __init__(self, level, treasures, MAZE_SIZE):
        """Constructs all the necessary attributes for the player object and turns on arrow key bindings."""
        turtle.Turtle.__init__(self)
        self.shape("player_right.gif")
        self.color("blue")
        self.penup()
        self.pensize(1)
        self.speed(0)
        self.score = 0
        self.level = level
        self.treasures = treasures
        self.MAZE_SIZE = MAZE_SIZE
        self.end_writer = writers.EndWriter(MAZE_SIZE)

        turtle.onkey(self.go_left, "Left")
        turtle.onkey(self.go_right, "Right")
        turtle.onkey(self.go_up, "Up")
        turtle.onkey(self.go_down, "Down")
        turtle.onkey(self.find_path, "f")

    def handle_event(self, coord_x, coord_y):
        j, i = utl.pixel_coords_to_pos(coord_x, coord_y, self.MAZE_SIZE)
        if self.level.in_maze(i, j):
            if self.level.maze[i][j] == 'X':
                return
            elif self.level.maze[i][j] == ' ':
                self.goto(coord_x, coord_y)
            elif self.level.maze[i][j] == 'P':
                self.goto(coord_x, coord_y)
            elif self.level.maze[i][j] == 'E':
                self.goto(coord_x, coord_y)
                self.end_writer.write(
                    f"You have won with {self.score} points! Do you want to play again? (y/n)", font=("Arial", 16, "normal"))
                self.end_game()
            elif self.level.maze[i][j] == 'T':
                self.score += 1
                self.goto(coord_x, coord_y)
                self.level.maze[i][j] = ' '
                self.treasures[(coord_x, coord_y)].destroy()

    def go_up(self):
        self.handle_event(self.xcor(), self.ycor() + BLOCK_PIXEL_SIZE)

    def go_down(self):
        self.handle_event(self.xcor(), self.ycor() - BLOCK_PIXEL_SIZE)

    def go_left(self):
        self.shape("player_left.gif")
        self.handle_event(self.xcor() - BLOCK_PIXEL_SIZE, self.ycor())

    def go_right(self):
        self.shape("player_right.gif")
        self.handle_event(self.xcor() + BLOCK_PIXEL_SIZE, self.ycor())

    def vizualize(self, moves):
        for move in moves:
            if move == 'L':
                self.go_left()
            elif move == 'R':
                self.go_right()
            elif move == 'D':
                self.go_down()
            elif move == 'U':
                self.go_up()

    def backtrack(self, maze, i, j, moves):
        if not self.level.in_maze(i, j):
            return
        elif maze[i][j] == 'X':
            return
        elif j == self.MAZE_SIZE-1:
            self.vizualize(moves)
            return
        else:
            maze[i][j] = 'X'
            moves.append('U')
            self.backtrack(maze, i-1, j, moves)
            moves.pop()
            moves.append('D')
            self.backtrack(maze, i+1, j, moves)
            moves.pop()
            moves.append('R')
            self.backtrack(maze, i, j+1, moves)
            moves.pop()
            moves.append('L')
            self.backtrack(maze, i, j-1, moves)
            moves.pop()
            maze[i][j] = ' '

    def find_path(self):
        j, i = utl.pixel_coords_to_pos(
            self.xcor(), self.ycor(), self.MAZE_SIZE)
        level_cpy = copy.deepcopy(self.level.maze)
        self.backtrack(level_cpy, i, j, [])

    def end_game(self):
        turtle.onkey(None, "Left")
        turtle.onkey(None, "Right")
        turtle.onkey(None, "Up")
        turtle.onkey(None, "Down")
