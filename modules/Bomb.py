import pygame
from modules.Game_Config import *
from modules import BombWave

IMAGES = [pygame.image.load("./data/images/boom1.png"),
          pygame.image.load("./data/images/boom2.png"),
          pygame.image.load("./data/images/boom3.png"),
          pygame.image.load("./data/images/boom4.png"),
          pygame.image.load("./data/images/boom5.png"),
          pygame.image.load("./data/images/boom6.png"),
          pygame.image.load("./data/images/boom7.png"),
          pygame.image.load("./data/images/boom8.png")]


class Bomb():

    def __init__(self, i, j, length, set_time) -> None:
        self.length = length
        self.j = j
        self.i = i
        self.set_time = set_time
        self.explore_time = set_time + 3*1000
        self.current_image = 0
        self.wave = BombWave.BombWave(self.i, self.j, self.length)

    def drawBombWave(self) -> None:
        self.wave.draw()

    def animations(self):
        speed = 0.1
        self.current_image += speed
        if(self.current_image >= 8):
            self.current_image = 0
        SCREEN.blit(pygame.transform.scale(IMAGES[int(self.current_image)], (S*6//5, S*8//5)),
                    (self.j*S + S/2 - S*0.1, self.i*S + S/2 - S*0.6))
