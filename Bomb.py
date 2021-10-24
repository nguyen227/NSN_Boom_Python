import pygame
from Game_Config import *
import BombWave

IMAGES = [(pygame.image.load("./data/images/boom1.png")),
          (pygame.image.load("./data/images/boom2.png")),
          (pygame.image.load("./data/images/boom3.png")),
          (pygame.image.load("./data/images/boom4.png")),
          (pygame.image.load("./data/images/boom5.png")),
          (pygame.image.load("./data/images/boom6.png")),
          (pygame.image.load("./data/images/boom7.png")),
          (pygame.image.load("./data/images/boom8.png"))]


class Bomb():

    def __init__(self, x, y, set_time) -> None:
        self.length = 3
        self.x = x
        self.y = y
        self.set_time = set_time
        self.explore_time = set_time + 2000
        self.current_image = 0
        self.wave = BombWave.BombWave(self.x, self.y, self.length)

    def drawBombWave(self) -> None:
        self.wave.draw()
        # pygame.display.update()

    def animations(self):
        speed = 0.1
        self.current_image += speed
        if(self.current_image >= 8):
            self.current_image = 0
        SCREEN.blit(IMAGES[int(self.current_image)],
                    (self.x*50 + 25 - 5, self.y*50 + 25 - 30))
        # pygame.display.update()


def reDraw():
    for i in BombsList:
        i.animations()
