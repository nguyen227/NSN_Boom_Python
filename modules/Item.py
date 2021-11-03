from random import randint

import pygame

from modules.Game_Config import *

IMAGES = [pygame.transform.scale(pygame.image.load("./data/images/item_capacity.png"), (S, S)),
          pygame.transform.scale(pygame.image.load(
              "./data/images/item_length.png"), (S, S)),
          pygame.transform.scale(pygame.image.load("./data/images/item_speed.png"), (S, S))]


class Item():
    def __init__(self, i, j) -> None:
        self.box = pygame.Rect(i*S+S, j*S+S, S, S)
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
                    (self.j*S+S/2, self.i*S+S/2+self.val))
