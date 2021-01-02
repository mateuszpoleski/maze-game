"""Main execute file for maze game."""
import turtle
from constants import BLOCK_PIXEL_SIZE
import utl
import maze

MAZE_SIZE = utl.take_user_input()
MAZE_PIXEL_SIZE = MAZE_SIZE * BLOCK_PIXEL_SIZE
SCREEN_SIZE = MAZE_PIXEL_SIZE + 100
MAZE_BORDER = ((MAZE_SIZE - 1) // 2) * BLOCK_PIXEL_SIZE

utl.screen_setup(SCREEN_SIZE)
utl.register_shapes()
utl.activate_keyboard_bindings()

game = maze.Maze(MAZE_SIZE)
game.start()

turtle.done()
