import turtle

import level
import player
import wall
import treasure
import writers
from constants import BLOCK_PIXEL_SIZE


class Maze:
    def __init__(self, MAZE_SIZE):
        self.treasures = {}
        self.level = level.Level(MAZE_SIZE)
        self.player = player.Player(self.level, self.treasures, MAZE_SIZE)
        self.start_writer = writers.StartWriter(MAZE_SIZE)
        self.wall = wall.Wall()

        self.MAZE_SIZE = MAZE_SIZE

    def setup_maze(self):
        MAZE_BORDER = ((self.MAZE_SIZE - 1) // 2) * BLOCK_PIXEL_SIZE
        for y in range(self.MAZE_SIZE):
            for x in range(self.MAZE_SIZE):
                character = self.level.maze[y][x]
                screen_x = -MAZE_BORDER + (x * BLOCK_PIXEL_SIZE)
                screen_y = MAZE_BORDER - (y * BLOCK_PIXEL_SIZE)

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
        self.start_writer.write(
            "R - restart  |  F - find path  |  E - exit", font=("Arial", 16, "normal"))
        self.level.create()
        self.setup_maze()
        turtle.onkey(self.reset, "r")
        turtle.onkey(self.reset, "y")

    def reset(self):
        turtle.resetscreen()
        for t in turtle.turtles():
            t.hideturtle()
        game = Maze(self.MAZE_SIZE)
        game.start()
