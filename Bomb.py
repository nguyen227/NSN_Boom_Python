import pygame
import main

BW_IMAGES = [(pygame.image.load('./data/images/bombbang_mid_2.png')),
             (pygame.image.load('./data/images/bombbang_up_1.png')),
             (pygame.image.load('./data/images/bombbang_up_2.png')),
             (pygame.image.load('./data/images/bombbang_down_1.png')),
             (pygame.image.load('./data/images/bombbang_down_2.png')),
             (pygame.image.load('./data/images/bombbang_left_1.png')),
             (pygame.image.load('./data/images/bombbang_left_2.png')),
             (pygame.image.load('./data/images/bombbang_right_1.png')),
             (pygame.image.load('./data/images/bombbang_right_2.png'))]

B_IMAGES = [(pygame.image.load("./data/images/boom1.png")),
            (pygame.image.load("./data/images/boom2.png")),
            (pygame.image.load("./data/images/boom3.png")),
            (pygame.image.load("./data/images/boom4.png")),
            (pygame.image.load("./data/images/boom5.png")),
            (pygame.image.load("./data/images/boom6.png")),
            (pygame.image.load("./data/images/boom7.png")),
            (pygame.image.load("./data/images/boom8.png"))]


class Bomb(pygame.sprite.Sprite):

    def __init__(self, x, y, set_time) -> None:
        self.length = 3
        self.x = x//50
        self.y = y//50
        self.set_time = set_time
        self.explore_time = set_time + 2000
        self.current_image = 0
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
        self.BombWave = [self.BombWaveMid, self.BombWaveUp,
                         self.BombWaveDown, self.BombWaveLeft, self.BombWaveRight]

    def drawBombWave(self) -> None:

        for Rect in self.BombWaveMid:
            main.WIN.blit(BW_IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveUp:
            main.WIN.blit(BW_IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveDown:
            main.WIN.blit(BW_IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveLeft:
            main.WIN.blit(BW_IMAGES[0], (Rect.x + 25, Rect.y + 25))
        for Rect in self.BombWaveRight:
            main.WIN.blit(BW_IMAGES[0], (Rect.x + 25, Rect.y + 25))
        pygame.display.update()

    def redrawBomb(self):
        speed = 0.1
        self.current_image += speed
        if(self.current_image >= 8):
            self.current_image = 0
        main.WIN.blit(B_IMAGES[int(self.current_image)],
                      (self.x*50 + 25 - 5, self.y*50 + 25 - 30))
        # pygame.display.update()
