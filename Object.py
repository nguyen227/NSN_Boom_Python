import pygame
import main
from Map import BITMAP

OBJECT_IMAGES = [(pygame.image.load("./data/images/0.png")),
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
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.box = pygame.Rect(25 + x*50, 25 + y*50, 50, 50)
        self.coTheDiQua = True if BITMAP[y][x] in (10, 0) else False
        self.breakable = False

    def draw(self):
        # pygame.display.update()
        main.WIN.blit(OBJECT_IMAGES[BITMAP[self.y][self.x]],
                      (25 + self.x*50, 25 + self.y*50))
        # main.WIN.blit(OBJECT_IMAGES[0 if BITMAP[self.y][self.x] == 0 else 11],
        #               (25 + self.x*50, 25 + self.y*50))
