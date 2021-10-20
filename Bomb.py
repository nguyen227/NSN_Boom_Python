import pygame


class Bomb():
    def __init__(self, x, y, time_set, parrent_surface) -> None:
        self.surface = parrent_surface
        self.length = 3
        self.x = x
        self.y = y
        self.time_set = time_set
        self.IMAGES = [(pygame.image.load('./data/images/bombbang_mid_2.png')),
                       (pygame.image.load('./data/images/bombbang_up_1.png')),
                       (pygame.image.load('./data/images/bombbang_up_2.png')),
                       (pygame.image.load('./data/images/bombbang_down_1.png')),
                       (pygame.image.load('./data/images/bombbang_down_2.png')),
                       (pygame.image.load('./data/images/bombbang_left_1.png')),
                       (pygame.image.load('./data/images/bombbang_left_2.png')),
                       (pygame.image.load('./data/images/bombbang_right_1.png')),
                       (pygame.image.load('./data/images/bombbang_right_2.png'))]
        self.BombWaveMid = [pygame.Rect(self.x*50, self.y*50, 50, 50)]
        self.BombWaveUp = []
        self.BombWaveDown = []
        self.BombWaveLeft = []
        self.BombWaveRight = []
        for i in range(1, self.length):
            self.BombWaveUp.append(pygame.Rect(
                self.x*50, (self.y-i)*50, 50, 50))
            self.BombWaveDown.append(pygame.Rect(
                self.x*50, (self.y+i)*50, 50, 50))
            self.BombWaveLeft.append(pygame.Rect(
                (self.x-i)*50, self.y*50, 50, 50))
            self.BombWaveRight.append(pygame.Rect(
                (self.x+i)*50, self.y*50, 50, 50))

    def drawBombWave(self) -> None:

        for Rect in self.BombWaveMid:
            self.surface.blit(self.IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveUp:
            self.surface.blit(self.IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveDown:
            self.surface.blit(self.IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveLeft:
            self.surface.blit(self.IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveRight:
            self.surface.blit(self.IMAGES[0], (Rect.x + 25, Rect.y + 25))
        pygame.display.update()
