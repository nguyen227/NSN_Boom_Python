import pygame


class Player():

    def __init__(self, x, y, width, height, parent_surface) -> None:
        self.surface = parent_surface
        self.playerRect = pygame.Rect(x, y, 50, 50)
        # self.x = x
        # self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.bombCapacity = 1
        self.PLAYER_IMAGE = pygame.image.load(
            './data/images/player_down_1.png')

    def draw(self) -> None:
        self.surface.blit(self.PLAYER_IMAGE,
                          (self.playerRect.x-7.5, self.playerRect.y - 30))
