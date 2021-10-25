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
    def __init__(self, i, j, length) -> None:
        self.length = length
        self.i = i
        self.j = j
        self.Mid = [(i, j)]
        self.Up = []
        self.Down = []
        self.Left = []
        self.Right = []

        for k in range(1, self.length):
            pos = (self.i-k, self.j)
            if not BombWave.canExploreTo(pos):
                break
            self.Up.append(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length):
            pos = (self.i+k, self.j)
            if not BombWave.canExploreTo(pos):
                break
            self.Down.append(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length):
            pos = (self.i, self.j-k)
            if not BombWave.canExploreTo(pos):
                break
            self.Left.append(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length):
            pos = (self.i, self.j+k)
            if not BombWave.canExploreTo(pos):
                break
            self.Right.append(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break
        self.BombWave = [self.Mid, self.Up, self.Down, self.Left, self.Right]

    def canExploreTo(pos):
        if ObjsList.get(pos):
            return ObjsList.get(pos).isBomb or ObjsList.get(pos).breakable
        else:
            if 0 <= pos[0] < 17 and 0 <= pos[1] < 17:
                return True
            return False

    def draw(self):
        for pos in self.Mid:
            SCREEN.blit(IMAGES[0], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        for pos in self.Up:
            SCREEN.blit(IMAGES[1], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        for pos in self.Down:
            SCREEN.blit(IMAGES[3], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        for pos in self.Left:
            SCREEN.blit(IMAGES[5], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        for pos in self.Right:
            SCREEN.blit(IMAGES[7], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0


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
