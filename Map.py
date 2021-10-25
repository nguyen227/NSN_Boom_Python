import Object
from Game_Config import *

file = open("./data/maps/level1.txt", "r")
map = file.readlines()
for i in range(len(map)):
    BitMap.append([int(x) for x in map[i].split()])
file.close()

for i in range(len(BitMap)):
    for j in range(len(BitMap[i])):
        if BitMap[i][j] != 0:
            ObjsList[(i, j)] = Object.Object(i, j)


def draw():
    for i in range(len(BitMap)):
        for j in range(len(BitMap[i])):
            if BitMap[i][j] != 0:
                ObjsList[(i, j)].draw()
