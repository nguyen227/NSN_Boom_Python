from random import randint
from modules import Object
from modules.Game_Config import *
# from Main import player1, player2


def load_map():
    BitMap.clear()
    lv = randint(1, 2)
    with open(f"./data/maps/map{lv}.txt", "r") as file:
        map = file.readlines()
        for i in range(len(map)):
            BitMap.append([int(x) for x in map[i].split()])


def update_objects():
    for i in range(len(BitMap)):
        for j in range(len(BitMap[i])):
            if BitMap[i][j] != 0:
                ObjsList[(i, j)] = Object.Object(i, j)
