import pygame, sys
from pygame.locals import *

GAME_CELL_SIZE_PX = 50  # HAVE TO BE EVEN NUMBER
assert (int(GAME_CELL_SIZE_PX/2)*2) == GAME_CELL_SIZE_PX

GAME_CELLS_X = 20
GAME_CELLS_Y = 15


def draw_segment(surface, x, y):
    """
    :param surface: surface to draw on
    :param x: x coord in game cells
    :param y: y coord in game cells
    :return: 
    """
    WHITE = (255, 255, 255)
    position = (
            x * GAME_CELL_SIZE_PX,
            y * GAME_CELL_SIZE_PX,
            GAME_CELL_SIZE_PX,
            GAME_CELL_SIZE_PX
    )
    pygame.draw.rect(surface, WHITE, position)


def draw_food(surface, x, y):
    """
    :param surface: surface to draw on
    :param x: x coord in game cells
    :param y: y coord in game cells
    :return: 
    """
    RED = (255, 0, 0)
    position = (
        x * GAME_CELL_SIZE_PX + GAME_CELL_SIZE_PX//2,
        y * GAME_CELL_SIZE_PX + GAME_CELL_SIZE_PX//2)
    pygame.draw.circle(surface, RED, position, GAME_CELL_SIZE_PX//2)


def run_game():
    pygame.init()
    # workaround for: https://github.com/pygame/pygame/issues/331
    pygame.mixer.quit()
    FPS = 60  # Frames Per Second
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(
        (GAME_CELLS_X * GAME_CELL_SIZE_PX, GAME_CELLS_Y * GAME_CELL_SIZE_PX)
    )
    pygame.display.set_caption('Segment and food')
    for x in range(GAME_CELLS_X):
        for y in range(GAME_CELLS_Y):
            if (x + y) % 2 == 0:
                draw_segment(surface=DISPLAYSURF, x=x, y=y)
            else:
                draw_food(surface=DISPLAYSURF, x=x, y=y)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    run_game()
