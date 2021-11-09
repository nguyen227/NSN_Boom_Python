import pygame
from modules.Game_Config import *

TYPES = {"start": 0}

IMAGES = [pygame.image.load("./data/images/startButton1.png"),
          pygame.image.load("./data/images/startButton2.png")]


class Button:
    def __init__(self, x, y, type) -> None:
        self.box = pygame.Rect(x, y, S*2.74, S*1.04)
        self.type = TYPES[type]

    def isOver(self, pos):
        return self.box.left <= pos[0] <= self.box.right and self.box.top <= pos[1] <= self.box.bottom

    def draw(self):
        if self.isOver(pygame.mouse.get_pos()):
            SCREEN.blit(pygame.transform.scale(
                IMAGES[self.type+1], (S*2.74, S*1.04)), (self.box.x, self.box.y))
        else:
            SCREEN.blit(pygame.transform.scale(
                IMAGES[self.type], (S*2.74, S*1.04)), (self.box.x, self.box.y))
