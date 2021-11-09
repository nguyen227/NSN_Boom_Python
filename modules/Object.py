from modules.Game_Config import *
import pygame

IMAGES = [pygame.image.load("./data/images/0.png"),
          pygame.image.load("./data/images/1.png"),
          pygame.image.load("./data/images/21.png"),
          pygame.image.load("./data/images/31.png"),
          pygame.image.load("./data/images/4.png"),
          pygame.image.load("./data/images/5.png"),
          pygame.image.load("./data/images/31.png"),
          pygame.image.load("./data/images/31.png"),
          pygame.image.load("./data/images/31.png"),
          pygame.image.load("./data/images/31.png"),
          pygame.image.load("./data/images/0.png"),
          pygame.image.load('./data/images/player_test.png')]


class Object():
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.box = pygame.Rect(S/2 + col*S, S/2 + row*S, S, S)
        self.canWalkThrough = True if BitMap[row][col] in (10, 0) else False
        self.breakable = True if BitMap[row][col] in (2, 4, 5) else False
        self.isBomb = False

    def draw(self):
        # Main
        SCREEN.blit(pygame.transform.scale(IMAGES[BitMap[self.row][self.col]], (S, S*1.4)),
                    (S/2 + self.col*S, S/2 + self.row*S-S*0.4))
        # Test
        # SCREEN.blit(IMAGES[0 if BitMap[self.row][self.col] == 0 else 11],
        #           (S/2 + self.col*S, S/2 + self.row*S-20))
