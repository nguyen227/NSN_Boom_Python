from random import randint

import pygame

from modules.Game_Config import *

IMAGES = [(pygame.image.load("./data/images/item_capacity.png")),
          (pygame.image.load("./data/images/item_length.png")),
          (pygame.image.load("./data/images/item_speed.png"))]


class Item():
    def __init__(self, i, j) -> None:
        self.box = pygame.Rect(i*50+50, j*50+50, 50, 50)
        self.i = i
        self.j = j
        self.type = randint(0, 2)

    def draw(self):
        SCREEN.blit(IMAGES[self.type], coordInGame((self.i, self.j)))
