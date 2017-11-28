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


class Snake:
    # A tu jest babol, ciekawe, czy ktoś ogarnie jaki
    vectors = {
        'UP': (0, 1),
        'DOWN': (0, -1),
        'LEFT': (-1, 0),
        'RIGHT': (1, 0),

    }

    def __init__(self):
        self.segments = [(0, 5), (1, 5), (2, 5)]
        self.direction = 'RIGHT'

    def move(self):
        vector = self.vectors.get(self.direction, (0, 0))
        # wypadałoby zalogować, że brakuje jakiegos klucza...
        self.segments.pop(0)
        first_segment = self.segments[-1]
        self.segments.append(
            # TODO: a może da się sprytniej? Coś z zip?
            (first_segment[0] + vector[0], first_segment[1] + vector[1])
        )

    def draw(self, surface):
        for segment in self.segments:
            draw_segment(surface, *segment)


def draw_background(surface):
    BLACK = (0, 0, 0)
    position = (
        0, 0,
        GAME_CELLS_X * GAME_CELL_SIZE_PX, GAME_CELLS_Y * GAME_CELL_SIZE_PX
    )
    pygame.draw.rect(surface, BLACK, position)


def run_game():
    pygame.init()
    # workaround for: https://github.com/pygame/pygame/issues/331
    pygame.mixer.quit()
    FPS = 10  # Frames Per Second
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(
        (GAME_CELLS_X * GAME_CELL_SIZE_PX, GAME_CELLS_Y * GAME_CELL_SIZE_PX)
    )
    pygame.display.set_caption('Moving segments with snake class')
    snake = Snake()
    while True:
        for event in pygame.event.get():
            print('event: {}'.format(event))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw_background(DISPLAYSURF)
        snake.draw(DISPLAYSURF)
        snake.move()
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    run_game()
