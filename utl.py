import turtle
from constants import BLOCK_PIXEL_SIZE
import maze


def register_shapes():
    turtle.register_shape("saphire.gif")
    turtle.register_shape("player_right.gif")
    turtle.register_shape("player_left.gif")
    turtle.register_shape("walls.gif")


def take_user_input():
    wn = turtle.Screen()
    wn.bgcolor("black")
    size = int(wn.textinput(
        "Maze Creation", "Size of the maze:"))
    if size % 2 == 0:
        size += 1
    return size


def screen_setup(SCREEN_SIZE):
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Maze Game")
    wn.setup(SCREEN_SIZE, SCREEN_SIZE)


def activate_keyboard_bindings():
    turtle.listen()
    turtle.onkey(exit, "e")
    turtle.onkey(exit, "n")


def pixel_coords_to_pos(i, j, MAZE_SIZE):
    MAZE_BORDER = ((MAZE_SIZE - 1) // 2) * BLOCK_PIXEL_SIZE
    pos_x = (i + MAZE_BORDER) // BLOCK_PIXEL_SIZE
    pos_y = (MAZE_BORDER - j) // BLOCK_PIXEL_SIZE

    return int(pos_x), int(pos_y)
