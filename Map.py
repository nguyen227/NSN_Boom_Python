import pygame
import Object
from Game_Config import *

file = open("./data/maps/level2.txt", "r")
map = file.readlines()
for i in range(len(map)):
    BITMAP.append([int(x) for x in map[i].split()])
file.close()

for i in range(len(BITMAP)):
    for j in range(len(BITMAP[i])):
        if BITMAP[i][j] != 0:
            objects[(i, j)] = Object.Object(j, i)


def draw():
    for i in range(len(BITMAP)):
        for j in range(len(BITMAP[i])):
            if BITMAP[i][j] != 0:
                objects[(i, j)].draw()