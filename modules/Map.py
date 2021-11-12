from modules import Object
from modules.Game_Config import *
import random
# from Main import player1, player2

mapFile = [
    "./data/maps/level1.txt",
    "./data/maps/level2.txt",
    "./data/maps/level3.txt",
    "./data/maps/level4.txt",
    "./data/maps/level5.txt"
]

mapPlay = random.choice(mapFile)
file = open(mapPlay, "r")
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
