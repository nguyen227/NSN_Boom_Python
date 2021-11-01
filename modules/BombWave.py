import pygame
from modules.Game_Config import *
from modules.Item import Item
from random import randint

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
        for k in range(1, self.length+1):
            pos = (self.i-k, self.j)
            if not BombWave.canExploreTo(pos):
                break
            self.Up.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length+1):
            pos = (self.i+k, self.j)
            if not BombWave.canExploreTo(pos):
                break
            self.Down.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length+1):
            pos = (self.i, self.j-k)
            if not BombWave.canExploreTo(pos):
                break
            self.Left.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break

        for k in range(1, self.length+1):
            pos = (self.i, self.j+k)
            if not BombWave.canExploreTo(pos):
                break
            self.Right.append(pos)
            self.Wave.add(pos)
            if ObjsList.get((pos[0], pos[1])) and ObjsList.get((pos[0], pos[1])).breakable:
                break
        # self.BombWave = [self.Mid, self.Up, self.Down, self.Left, self.Right]

    def ObjectExplored(pos):
        if ObjsList.get(pos) and ObjsList.get(pos).breakable:
            ObjsList.pop(pos)
            BitMap[pos[0]][pos[1]] = 0
        if randint(0, 1) == 1:
            ItemsList[pos] = Item(pos[0], pos[1])

    def draw(self):

        # WaveMid_Animations
        for pos in self.Mid:
            SCREEN.blit(IMAGES[0], (coordInGame(pos)))

        # WaveUP_Animations
        for pos in self.Up:
            SCREEN.blit(IMAGES[1], (coordInGame(pos)))
        if len(self.Up) > 0:
            if ObjsList.get(self.Up[-1]) and ObjsList.get(self.Up[-1]).breakable:
                BombWave.ObjectExplored(self.Up[-1])
            SCREEN.blit(IMAGES[2], (coordInGame(self.Up[-1])))

        # WaveDOWN_Animations
        for pos in self.Down:
            SCREEN.blit(IMAGES[3], (coordInGame(pos)))
        if len(self.Down) > 0:
            if ObjsList.get(self.Down[-1]) and ObjsList.get(self.Down[-1]).breakable:
                BombWave.ObjectExplored(self.Down[-1])
            SCREEN.blit(IMAGES[4], (coordInGame(self.Down[-1])))

        # WaveLEFT_Animations
        for pos in self.Left:
            SCREEN.blit(IMAGES[5], (coordInGame(pos)))
        if len(self.Left) > 0:
            if ObjsList.get(self.Left[-1]) and ObjsList.get(self.Left[-1]).breakable:
                BombWave.ObjectExplored(self.Left[-1])
            SCREEN.blit(IMAGES[6], (coordInGame(self.Left[-1])))

        # WaveRIGHT_Animations
        for pos in self.Right:
            SCREEN.blit(IMAGES[7], (coordInGame(pos)))
        if len(self.Right) > 0:
            if ObjsList.get(self.Right[-1]) and ObjsList.get(self.Right[-1]).breakable:
                BombWave.ObjectExplored(self.Right[-1])
            SCREEN.blit(IMAGES[8], (coordInGame(self.Right[-1])))


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
