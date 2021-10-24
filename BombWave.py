import pygame
from Game_Config import *


IMAGES = [(pygame.image.load('./data/images/bombbang_mid_2.png')),
          (pygame.image.load('./data/images/bombbang_up_1.png')),
          (pygame.image.load('./data/images/bombbang_up_2.png')),
          (pygame.image.load('./data/images/bombbang_down_1.png')),
          (pygame.image.load('./data/images/bombbang_down_2.png')),
          (pygame.image.load('./data/images/bombbang_left_1.png')),
          (pygame.image.load('./data/images/bombbang_left_2.png')),
          (pygame.image.load('./data/images/bombbang_right_1.png')),
          (pygame.image.load('./data/images/bombbang_right_2.png'))]


class BombWave():
    def __init__(self, j, i, length) -> None:
        self.length = length
        self.x = j
        self.y = i
        self.Mid = [pygame.Rect(self.x*50+25, self.y*50+25, 50, 50)]
        self.Up = []
        self.Down = []
        self.Left = []
        self.Right = []
        for i in range(1, self.length):
            self.Up.append(pygame.Rect(
                self.x*50+25, (self.y-i)*50+25, 50, 50))
            self.Down.append(pygame.Rect(
                self.x*50 + 25, (self.y+i)*50 + 25, 50, 50))
            self.Left.append(pygame.Rect(
                (self.x-i)*50 + 25, self.y*50 + 25, 50, 50))
            self.Right.append(pygame.Rect(
                (self.x+i)*50 + 25, self.y*50 + 25, 50, 50))
        self.BombWave = [self.Mid, self.Up,
                         self.Down, self.Left, self.Right]

    def canExploreTo(Rect):
        posInMatrix = ((Rect.y-25)//50, (Rect.x-25)//50)
        if ObjsList.get(posInMatrix):
            return ObjsList.get(posInMatrix).isBomb or ObjsList.get(posInMatrix).breakable
            # return Rect.colliderect(ObjsList[(((Rect.y-25)//50, (Rect.x-25)//50))].box)
        else:
            if 0 <= (Rect.y-25)//50 < 17 and 0 <= (Rect.x-25)//50 < 17:
                return True
            return False

    def draw(self):
        for Rect in self.Mid:
            SCREEN.blit(IMAGES[0], (Rect.x, Rect.y))
        for Rect in self.Up:
            if not BombWave.canExploreTo(Rect):
                break
            SCREEN.blit(IMAGES[1], (Rect.x, Rect.y))
            if ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)) and ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)).breakable:
                ObjsList.pop(((Rect.y-25)//50, (Rect.x-25)//50))
                BitMap[(Rect.y-25)//50][(Rect.x-25)//50] = 0
                break
        for Rect in self.Down:
            if not BombWave.canExploreTo(Rect):
                break
            SCREEN.blit(IMAGES[3], (Rect.x, Rect.y))
            if ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)) and ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)).breakable:
                ObjsList.pop(((Rect.y-25)//50, (Rect.x-25)//50))
                BitMap[(Rect.y-25)//50][(Rect.x-25)//50] = 0
                break
        for Rect in self.Left:
            if not BombWave.canExploreTo(Rect):
                break
            SCREEN.blit(IMAGES[5], (Rect.x, Rect.y))
            if ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)) and ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)).breakable:
                ObjsList.pop(((Rect.y-25)//50, (Rect.x-25)//50))
                BitMap[(Rect.y-25)//50][(Rect.x-25)//50] = 0
                break
        for Rect in self.Right:
            if not BombWave.canExploreTo(Rect):
                break
            SCREEN.blit(IMAGES[7], (Rect.x, Rect.y))
            if ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)) and ObjsList.get(((Rect.y-25)//50, (Rect.x-25)//50)).breakable:
                ObjsList.pop(((Rect.y-25)//50, (Rect.x-25)//50))
                BitMap[(Rect.y-25)//50][(Rect.x-25)//50] = 0
                break
        # pygame.display.update()
        # pygame.time.wait(1000)


def reDraw():
    # Remove bomb completely explored
    for bomb in ExploringBomb:
        if pygame.time.get_ticks() - bomb.explore_time > 2 * 1000:
            ExploringBomb.pop(ExploringBomb.index(bomb))
        else:
            break
    #  Draw exploring bomb
    for bomb in ExploringBomb:
        if pygame.time.get_ticks() - bomb.explore_time <= 2 * 1000:
            bomb.drawBombWave()
