import pygame
from Game_Config import *


BW_IMAGES = [(pygame.image.load('./data/images/bombbang_mid_2.png')),
             (pygame.image.load('./data/images/bombbang_up_1.png')),
             (pygame.image.load('./data/images/bombbang_up_2.png')),
             (pygame.image.load('./data/images/bombbang_down_1.png')),
             (pygame.image.load('./data/images/bombbang_down_2.png')),
             (pygame.image.load('./data/images/bombbang_left_1.png')),
             (pygame.image.load('./data/images/bombbang_left_2.png')),
             (pygame.image.load('./data/images/bombbang_right_1.png')),
             (pygame.image.load('./data/images/bombbang_right_2.png'))]


class BombWave():
    def __init__(self, x, y, length) -> None:
        self.length = length
        self.x = x
        self.y = y
        self.BombWaveMid = [pygame.Rect(self.x*50+25, self.y*50+25, 50, 50)]
        self.BombWaveUp = []
        self.BombWaveDown = []
        self.BombWaveLeft = []
        self.BombWaveRight = []
        for i in range(1, self.length):
            self.BombWaveUp.append(pygame.Rect(
                self.x*50+25, (self.y-i)*50+25, 50, 50))
            self.BombWaveDown.append(pygame.Rect(
                self.x*50 + 25, (self.y+i)*50 + 25, 50, 50))
            self.BombWaveLeft.append(pygame.Rect(
                (self.x-i)*50 + 25, self.y*50 + 25, 50, 50))
            self.BombWaveRight.append(pygame.Rect(
                (self.x+i)*50 + 25, self.y*50 + 25, 50, 50))
        self.BombWave = [self.BombWaveMid, self.BombWaveUp,
                         self.BombWaveDown, self.BombWaveLeft, self.BombWaveRight]

    def draw(self):
        for Rect in self.BombWaveMid:
            SCREEN.blit(BW_IMAGES[0], (Rect.x, Rect.y))
        for Rect in self.BombWaveUp:
            if objects.get(((Rect.y-25)//50, (Rect.x-25)//50)) and Rect.colliderect(objects[(((Rect.y-25)//50, (Rect.x-25)//50))].box):
                break
            SCREEN.blit(BW_IMAGES[1], (Rect.x, Rect.y))
        for Rect in self.BombWaveDown:
            if objects.get(((Rect.y-25)//50, (Rect.x-25)//50)) and Rect.colliderect(objects[(((Rect.y-25)//50, (Rect.x-25)//50))].box):
                break
            SCREEN.blit(BW_IMAGES[3], (Rect.x, Rect.y))
        for Rect in self.BombWaveLeft:
            if objects.get(((Rect.y-25)//50, (Rect.x-25)//50)) and Rect.colliderect(objects[(((Rect.y-25)//50, (Rect.x-25)//50))].box):
                break
            SCREEN.blit(BW_IMAGES[5], (Rect.x, Rect.y))
        for Rect in self.BombWaveRight:
            if objects.get(((Rect.y-25)//50, (Rect.x-25)//50)) and Rect.colliderect(objects[(((Rect.y-25)//50, (Rect.x-25)//50))].box):
                break
            SCREEN.blit(BW_IMAGES[7], (Rect.x, Rect.y))
        # pygame.display.update()
        # pygame.time.delay(2000)
