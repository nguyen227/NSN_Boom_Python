import pygame
from modules.Game_Config import *


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
        self.Mid = [(self.i, self.j)]
        self.Up = []
        self.Down = []
        self.Left = []
        self.Right = []
        self.Wave = {(i, j)}
        self.createBombWave()

    def canExploreTo(pos):
        if ObjsList.get(pos):
            return ObjsList.get(pos).isBomb or ObjsList.get(pos).breakable
        else:
            if 0 <= pos[0] < 17 and 0 <= pos[1] < 17:
                return True
            return False

    def createBombWave(self):
        for k in range(1, self.length):
            pos = (self.i-k, self.j)
            if not BombWave.canExploreTo(pos):
                break
            self.Up.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length):
            pos = (self.i+k, self.j)
            if not BombWave.canExploreTo(pos):
                break
            self.Down.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length):
            pos = (self.i, self.j-k)
            if not BombWave.canExploreTo(pos):
                break
            self.Left.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length):
            pos = (self.i, self.j+k)
            if not BombWave.canExploreTo(pos):
                break
            self.Right.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break
        # self.BombWave = [self.Mid, self.Up, self.Down, self.Left, self.Right]

    def draw(self):
        for pos in self.Mid:
            SCREEN.blit(IMAGES[0], (pos[1]*50+25, pos[0]*50+25))
        for pos in self.Up:
            SCREEN.blit(IMAGES[1], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        if len(self.Up) > 0:
            SCREEN.blit(IMAGES[2], (self.Up[-1][1] *
                        50+25, self.Up[-1][0]*50+25))
        for pos in self.Down:
            SCREEN.blit(IMAGES[3], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        if len(self.Down) > 0:
            SCREEN.blit(IMAGES[4], (self.Down[-1][1] *
                                    50+25, self.Down[-1][0]*50+25))
        for pos in self.Left:
            SCREEN.blit(IMAGES[5], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        if len(self.Left) > 0:
            SCREEN.blit(IMAGES[6], (self.Left[-1][1] *
                                    50+25, self.Left[-1][0]*50+25))
        for pos in self.Right:
            SCREEN.blit(IMAGES[7], (pos[1]*50+25, pos[0]*50+25))
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                ObjsList.pop((pos[0], pos[1]))
                BitMap[pos[0]][pos[1]] = 0
        if len(self.Right) > 0:
            SCREEN.blit(IMAGES[8], (self.Right[-1][1] *
                                    50+25, self.Right[-1][0]*50+25))


def reDraw():
    # Remove bomb completely explored
    for bomb in ExploringBomb:
        if pygame.time.get_ticks() - bomb.explore_time > 0.5 * 1000:
            # print(pygame.time.get_ticks())
            ExploringBomb.pop(ExploringBomb.index(bomb))
        else:
            break
    #  Draw exploring bomb
    for bomb in ExploringBomb:
        if pygame.time.get_ticks() - bomb.explore_time <= 0.5 * 1000:
            bomb.drawBombWave()
