import pygame

BITMAP = []
file = open("./data/maps/level2.txt", "r")
map = file.readlines()
for i in range(len(map)):
    BITMAP.append([int(x) for x in map[i].split()])
file.close()


def draw():
    for i in range(len(BITMAP)):
        for j in range(len(BITMAP[i])):
            if BITMAP[i][j] != 0 and BITMAP[i][j] != 10:
                objects.append(pygame.Rect(GAME_AREA.x + j *
                               50, GAME_AREA.y + i*50, 50, 50))
            WIN.blit(OBJECT_IMAGES[BITMAP[i][j]],
                     (GAME_AREA.x + j*50, GAME_AREA.y + i*50))
