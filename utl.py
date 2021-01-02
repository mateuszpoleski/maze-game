"""File with various useful functions that are used in the project."""
import turtle
from constants import BLOCK_PIXEL_SIZE


def register_shapes():
    """Register turtle shapes of graphics in project."""
    turtle.Screen().register_shape("saphire.gif")
    turtle.Screen().register_shape("player_right.gif")
    turtle.Screen().register_shape("player_left.gif")
    turtle.Screen().register_shape("walls.gif")


def take_user_input():
    """Take user input of maze size. If size is even add one to it."""
    window = turtle.Screen()
    window.bgcolor("black")
    size = int(window.textinput(
        "Maze Creation", "Size of the maze:"))
    if size % 2 == 0:
        size += 1
    return size


def screen_setup(screen_size):
    """Setup turtle screen of given size."""
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Maze Game")
    window.setup(screen_size, screen_size)


def activate_keyboard_bindings():
    """Activate keyboard bindings and listener."""
    turtle.Screen().listen()
    turtle.Screen().onkey(exit, "e")
    turtle.Screen().onkey(exit, "n")


def pixel_coords_to_pos(i, j, maze_size):
    """Return position in maze given pixel coords."""
    maze_border = ((maze_size - 1) // 2) * BLOCK_PIXEL_SIZE
    pos_x = (i + maze_border) // BLOCK_PIXEL_SIZE
    pos_y = (maze_border - j) // BLOCK_PIXEL_SIZE

    return int(pos_x), int(pos_y)

def in_range(i, j, size):
    """Return if given coords are insade a size:size aray."""
    return 0 <= i < size and 0 <= j < size
