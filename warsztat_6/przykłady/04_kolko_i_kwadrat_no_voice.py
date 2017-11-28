import pygame, sys
from pygame.locals import *


# RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
# workaround for: https://github.com/pygame/pygame/issues/331
pygame.mixer.quit()
FPS = 60  # Frames Per Second
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Circle and the square!')

# x, y (lewy górny róg), szerokość, wysokość
pygame.draw.rect(DISPLAYSURF, WHITE, (100, 100, 50, 50))
# (x, y), promień, grubość
pygame.draw.circle(DISPLAYSURF, RED, (200, 150), 50)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
