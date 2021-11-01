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

        # Animations
        self.dir = 1  # 1 Down, -1 Up
        self.val = 0

    def draw(self):
        self.val += self.dir * 0.5
        if self.val > 0:
            self.val = 0
            self.dir *= -1
        if self.val < -20:
            self.val = -20
            self.dir *= -1
        SCREEN.blit(IMAGES[self.type],
                    (self.j*50+25, self.i*50+25+self.val))
