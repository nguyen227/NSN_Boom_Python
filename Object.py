import pygame
from Game_Config import *

IMAGES = [(pygame.image.load("./data/images/0.png")),
          (pygame.transform.scale(pygame.image.load(
              "./data/images/1.png"), (50, 71))),
          (pygame.image.load("./data/images/2.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/4.png")),
          (pygame.image.load("./data/images/5.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/0.png")),
          (pygame.image.load('./data/images/player_test.png'))]


class Object():
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.box = pygame.Rect(25 + col*50, 25 + row*50, 50, 50)
        self.canWalkThrough = True if BitMap[row][col] in (10, 0) else False
        self.breakable = True if BitMap[row][col] in (2, 4, 5) else False
        self.isBomb = False

    def draw(self):
        # Main
        SCREEN.blit(IMAGES[BitMap[self.row][self.col]],
                    (25 + self.col*50, 25 + self.row*50))
        # Test
        # SCREEN.blit(IMAGES[0 if Map.BitMap[self.row][self.col] == 0 else 11],
        #             (25 + self.col*50, 25 + self.row*50))
