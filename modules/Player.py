import pygame
from modules.Game_Config import *
from modules import Bomb, Object
import math

IMAGES = [(pygame.image.load('./data/images/player_down_1.png')),
          ]


class Player():

    def __init__(self, x, y, width, height) -> None:
        self.box = pygame.Rect(x, y, 50, 50)
        # Player.set_previous_pos(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 3
        self.bombCapacity = 4
        self.current_sprite = 0
        self.image = IMAGES[self.current_sprite]
        self.bombsList = {}

    def draw(self) -> None:
        SCREEN.blit(self.image, (self.box.x-7.5, self.box.y-30))  # Main
        # SCREEN.blit(self.image, (self.box.x, self.box.y))  # Test

    def distance(self, coordinate):
        x1, y1 = self.box.center
        y2, x2 = coordinate
        # print(player1.box.center, coordinate)
        return math.sqrt(((x2*50+50.0)-x1)**2 + ((y2*50+50.0) - y1)**2)

    def datBomb(self):
        i, j = self.box.y//50, self.box.x//50
        if BitMap[i][j] != 0:
            return
        self.bombCapacity -= 1
        BombsList.append(Bomb.Bomb(i, j, pygame.time.get_ticks()))
        # i, j = BombsList[-1].y, BombsList[-1].x
        BitMap[i][j] = 10
        ObjsList[(i, j)] = Object.Object(i, j)
        ObjsList[(i, j)].isBomb = True
        CanWalkThrough.append((i, j))

    def handle_movement(self, keys_pressed):
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
