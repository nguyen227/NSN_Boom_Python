import pygame
import main


class Player():

    def __init__(self, x, y, width, height) -> None:
        self.box = pygame.Rect(x, y, 50, 50)
        Player.set_previous_pos(self)
        # self.x = x
        # self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.bombCapacity = 3
        self.PLAYER_IMAGE = pygame.image.load(
            './data/images/player_down_1.png')
        self.bombsList = {}

    def draw(self) -> None:
        main.WIN.blit(self.PLAYER_IMAGE,
                      (self.box.x-7.5, self.box.y-30))

    def get_current_pos(self):
        return ((self.box.x-25) // 50, (self.box.y-25)//50)

    def set_previous_pos(self):
        self.previous_pos = ((self.box.x-25) // 50, (self.box.y-25)//50)
