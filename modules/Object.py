import pygame
from modules.Game_Config import *

IMAGES = [(pygame.image.load("./data/images/0.png")),
          (pygame.image.load("./data/images/1.png")),
          (pygame.image.load("./data/images/21.png")),
          (pygame.image.load("./data/images/31.png")),
          (pygame.image.load("./data/images/41.png")),
          (pygame.image.load("./data/images/51.png")),
          (pygame.image.load("./data/images/31.png")),
          (pygame.image.load("./data/images/31.png")),
          (pygame.image.load("./data/images/31.png")),
          (pygame.image.load("./data/images/31.png")),
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
                    (25 + self.col*50, 25 + self.row*50-20))
        # Test
        # SCREEN.blit(IMAGES[0 if BitMap[self.row][self.col] == 0 else 11],
        #           (25 + self.col*50, 25 + self.row*50-20))
