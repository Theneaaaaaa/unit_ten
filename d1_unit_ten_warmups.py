import pygame, sys
from pygame.locals import *
import logo


pygame.init()
mainSurface = pygame.display.set_mode((600, 500), 0, 32)
pygame.display.set_caption("Pygame Test Window")
ssfs = logo.Logo(mainSurface)
ssfs.draw_rectangles()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
