"""File with implementation of Player class."""
import copy
import turtle
import utl
import writers
from constants import BLOCK_PIXEL_SIZE


class Player(turtle.Turtle):
    """A class to represent a player of the game."""

    def __init__(self, level, treasures, maze_size):
        """
        Constructs all the necessary attributes for the player object.
        Turn on arrow key bindings.
        """
        turtle.Turtle.__init__(self)
        self.shape("player_right.gif")
        self.color("blue")
        self.penup()
        self.pensize(1)
        self.speed(0)
        self.score = 0
        self.level = level
        self.treasures = treasures
        self.maze_size = maze_size
        self.end_writer = writers.EndWriter(maze_size)

        turtle.Screen().onkey(self.go_left, "Left")
        turtle.Screen().onkey(self.go_right, "Right")
        turtle.Screen().onkey(self.go_up, "Up")
        turtle.Screen().onkey(self.go_down, "Down")
        turtle.Screen().onkey(self.find_path, "f")

    def handle_event(self, coord_x, coord_y):
        """Handle even on different types of poles in a maze."""
        j, i = utl.pixel_coords_to_pos(coord_x, coord_y, self.maze_size)
        if self.level.in_maze(i, j):
            if self.level.maze[i][j] == ' ':
                self.goto(coord_x, coord_y)
            elif self.level.maze[i][j] == 'P':
                self.goto(coord_x, coord_y)
            elif self.level.maze[i][j] == 'E':
                self.goto(coord_x, coord_y)
                self.end_game()
            elif self.level.maze[i][j] == 'T':
                self.score += 1
                self.goto(coord_x, coord_y)
                self.level.maze[i][j] = ' '
                self.treasures[(coord_x, coord_y)].destroy()

    def go_up(self):
        """Move player up."""
        self.handle_event(self.xcor(), self.ycor() + BLOCK_PIXEL_SIZE)

    def go_down(self):
        """Move player down."""
        self.handle_event(self.xcor(), self.ycor() - BLOCK_PIXEL_SIZE)

    def go_left(self):
        """Move player left."""
        self.shape("player_left.gif")
        self.handle_event(self.xcor() - BLOCK_PIXEL_SIZE, self.ycor())

    def go_right(self):
        """Move player right."""
        self.shape("player_right.gif")
        self.handle_event(self.xcor() + BLOCK_PIXEL_SIZE, self.ycor())

    def vizualize(self, moves):
        """
        Make sequence of moves.

        moves -- list of moves
        """
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
        """Backtrack to find solution of the maze for the given player coords."""
        if not self.level.in_maze(i, j):
            return
        if maze[i][j] == 'X':
            return
        if j == self.maze_size-1:
            self.vizualize(moves)
            return

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
        """Find and vizualize solution for the maze."""
        j, i = utl.pixel_coords_to_pos(
            self.xcor(), self.ycor(), self.maze_size)
        level_cpy = copy.deepcopy(self.level.maze)
        self.backtrack(level_cpy, i, j, [])

    def end_game(self):
        """Actions to make after player finishes the game."""
        self.end_writer.write(f"You have won with {self.score} points! " \
                               "Do you want to play again? (y/n)", font=("Arial", 16, "normal"))
        turtle.Screen().onkey(None, "Left")
        turtle.Screen().onkey(None, "Right")
        turtle.Screen().onkey(None, "Up")
        turtle.Screen().onkey(None, "Down")
