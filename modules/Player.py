import pygame
from pygame import key
from modules.Game_Config import *
from modules import Bomb, Object
import math

from modules.Item import Item

IMAGES = [(pygame.image.load('./data/images/player_down_1.png')),
          ]


class Player():

    def __init__(self, x, y) -> None:
        self.box = pygame.Rect(x, y, 50, 50)
        self.speed = 2
        self.bombCapacity = 1
        self.bombLength = 1

        # Animations
        self.current_sprite = 0
        self.image = IMAGES[self.current_sprite]

    def get_pos(self):
        return ((self.box.centery - 25) // 50, (self.box.centerx - 25) // 50)

    def draw(self) -> None:
        SCREEN.blit(self.image, (self.box.x-7.5, self.box.y-30))  # Main
        # SCREEN.blit(self.image, (self.box.x, self.box.y))  # Test

    def distance(self, coordinate):
        x1, y1 = self.box.center
        y2, x2 = coordinate
        return math.sqrt(((x2*50+50.0)-x1)**2 + ((y2*50+50.0) - y1)**2)

# _______________________________________________________________________________________\
# HANDLE_BOMB____________________________________________________________________________\
# _______________________________________________________________________________________\
    def set_Bomb(self):
        i, j = self.box.y//50, self.box.x//50
        if self.bombCapacity == 0 or BitMap[i][j] != 0:
            return
        self.bombCapacity -= 1
        BombsList.append(
            Bomb.Bomb(i, j, self.bombLength, pygame.time.get_ticks()))
        BitMap[i][j] = 10
        ObjsList[(i, j)] = Object.Object(i, j)
        ObjsList[(i, j)].isBomb = True
        CanWalkThrough.append((i, j))

    def handleBomb(self):
        for obj in CanWalkThrough:
            if ObjsList.get(obj):
                # print(distance(obj))
                if self.distance(obj) > 49:
                    ObjsList[(obj)].canWalkThrough = False
                    CanWalkThrough.pop(CanWalkThrough.index(obj))
            else:
                CanWalkThrough.pop(CanWalkThrough.index(obj))

        if len(BombsList) > 0 and pygame.time.get_ticks() > BombsList[0].explore_time:
            # print(pygame.time.get_ticks())
            BitMap[BombsList[0].i][BombsList[0].j] = 0
            ObjsList.pop((BombsList[0].i, BombsList[0].j))
            self.bombCapacity += 1
            ExploringBomb.append(BombsList.pop(0))
            for bomb in BombsList:
                if (ExploringBomb[-1].i, ExploringBomb[-1].j) in bomb.wave.Wave:
                    bomb.explore_time = ExploringBomb[-1].explore_time


# _______________________________________________________________________________________\
# HANDLE_MOVEMENT________________________________________________________________________\
# _______________________________________________________________________________________\


    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:  # MOVE LEFT
            self.move_left()
        if keys_pressed[pygame.K_RIGHT]:  # MOVE RIGHT
            self.move_right()
        if keys_pressed[pygame.K_UP]:  # MOVE UP
            self.move_up()
        if keys_pressed[pygame.K_DOWN]:  # MOVE DOWN
            self.move_down()

    def canMoveTo(i, j):
        return ObjsList.get((i, j)).canWalkThrough if ObjsList.get((i, j)) else True

    def move_left(self):
        x = self.box.x - 25
        y = self.box.y - 25
        for i in range(self.speed, 0, -1):
            x1 = x - i
            if y + 49 > 850 or x1 + 49 > 850 or y < 0 or x1 < 0:
                continue
            if Player.canMoveTo(y//50, x1//50) and not Player.canMoveTo((y+49)//50, x1//50):
                if y+49 - ((y+49)//50*50) < self.speed:
                    self.box.y -= y + 50 - ((y+49)//50*50)
                    self.box.x -= i
                    return
            elif not Player.canMoveTo(y//50, x1//50) and Player.canMoveTo((y+49)//50, x1//50):
                if (y//50*50+49) - y < self.speed:
                    self.box.y += (y//50*50+50) - y
                    self.box.x -= i
                    return
            elif Player.canMoveTo(y//50, x1//50) and Player.canMoveTo((y+49)//50, x1//50):
                self.box.x -= i
                return

    def move_right(self):
        x = self.box.x - 25
        y = self.box.y - 25
        for i in range(self.speed, 0, -1):
            x1 = x + i
            if y + 49 >= 850 or x1 + 49 >= 850 or y < 0 or x1 < 0:
                continue
            if Player.canMoveTo(y//50, (x1+49)//50) and not Player.canMoveTo((y+49)//50, (x1+49)//50):
                if y+49 - ((y+49)//50*50) < self.speed:
                    self.box.y -= y + 50 - ((y+49)//50*50)
                    self.box.x += i
                    return
            elif not Player.canMoveTo(y//50, (x1+49)//50) and Player.canMoveTo((y+49)//50, (x1+49)//50):
                if (y//50*50+49) - y < self.speed:
                    self.box.y += (y//50*50+50) - y
                    self.box.x += i
                    return
            elif Player.canMoveTo(y//50, (x1+49)//50) and Player.canMoveTo((y+49)//50, (x1+49)//50):
                self.box.x += i
                return

    def move_up(self):
        x = self.box.x - 25
        y = self.box.y - 25
        for i in range(self.speed, 0, -1):
            y1 = y - i
            if y1 + 49 >= 850 or x + 49 >= 850 or y1 < 0 or x < 0:
                continue
            if Player.canMoveTo(y1//50, x//50) and not Player.canMoveTo(y1//50, (x+49)//50):
                if x+49 - ((x+49)//50*50) < self.speed:
                    self.box.x -= x + 50 - ((x+49)//50*50)
                    self.box.y -= i
                    return
            elif not Player.canMoveTo(y1//50, x//50) and Player.canMoveTo(y1//50, (x+49)//50):
                if (x//50*50+49) - x < self.speed:
                    self.box.x += (x//50*50+50) - x
                    self.box.y -= i
                    return
            elif Player.canMoveTo(y1//50, x//50) and Player.canMoveTo(y1//50, (x+49)//50):
                self.box.y -= i
                return

    def move_down(self):
        x = self.box.x - 25
        y = self.box.y - 25
        for i in range(self.speed, 0, -1):
            y1 = y + i
            if y1 + 49 >= 850 or x + 49 >= 850 or y1 < 0 or x < 0:
                continue
            if Player.canMoveTo((y1+49)//50, x//50) and not Player.canMoveTo((y1+49)//50, (x+49)//50):
                if x+49 - ((x+49)//50*50) < self.speed:
                    self.box.x -= x + 50 - ((x+49)//50*50)
                    self.box.y += i
                    return
            elif not Player.canMoveTo((y1+49)//50, x//50) and Player.canMoveTo((y1+49)//50, (x+49)//50):
                if (x//50*50+49) - x < self.speed:
                    self.box.x += (x//50*50+50) - x
                    self.box.y += i
                    return
            elif Player.canMoveTo((y1+49)//50, x//50) and Player.canMoveTo((y1+49)//50, (x+49)//50):
                self.box.y += i
                return
        return 0

# _______________________________________________________________________________________\
# HANDLE_ITEM____________________________________________________________________________\
# _______________________________________________________________________________________\
    def handle_item(self):
        if ItemsList.get(self.get_pos()):
            if ItemsList[self.get_pos()].type == 0 and self.bombCapacity < 7:
                self.bombCapacity += 1
            elif ItemsList[self.get_pos()].type == 1 and self.bombLength < 7:
                self.bombLength += 1
            elif ItemsList[self.get_pos()].type == 2 and self.speed < 10:
                self.speed += 1
            ItemsList.pop(self.get_pos())
