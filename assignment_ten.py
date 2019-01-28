# Thenea Sun
# Dec.7th
# Create a face that will consist of a round circle for the head, a triangle for the nose, two additional circles for
# the eyes, and a rectangle for the mouth, it will draw an instance of the face wherever the mouse is clicked.
import pygame, sys
from pygame.locals import *
import random


class Draw:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.GREEN = (0, 102, 71)
        self.GOLD = (255, 209, 63)
        self.WHITE = (255, 255, 255)
        self.WHITE = (255, 255, 255)
        self.PINK = (255, 192, 203)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.colors = [self.GOLD, self.GREEN, self.PINK, self.WHITE, self.RED, self.BLUE]

    def draw(self, mouse_position):
        x_pos = mouse_position[0]
        y_pos = mouse_position[1]

# Make a basic shape for the face
        pygame.draw.circle(mainSurface, random.choice(self.colors), (x_pos, y_pos), 75, 0)
        pygame.display.update()
        pygame.draw.rect(mainSurface, random.choice(self.colors), (x_pos - 35, y_pos + 20, 75, 30), 0)
        pygame.display.update()
        pygame.draw.polygon(mainSurface, random.choice(self.colors), ((x_pos, y_pos - 10), (x_pos + 25, y_pos + 10),
                                                                      (x_pos - 20, y_pos + 10)), 0)
        pygame.draw.circle(mainSurface, random.choice(self.colors), (x_pos - 35, y_pos - 30), 20, 0)
        pygame.draw.circle(mainSurface, random.choice(self.colors), (x_pos + 35, y_pos - 30), 20, 0)
        pygame.display.update()


pygame.init()
mainSurface = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption("Draw faces 1.0")
face = Draw(mainSurface)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            face.draw(pygame.mouse.get_pos())
