
import pygame
from pygame import key

import Bomb
import BombWave
import Colors
import Map
import Player
from Game_Config import *

player1 = Player.Player(75, 75, 50, 50)


def draw_window():
    SCREEN.fill(Colors.BLUE)
    SCREEN.blit(BACKGROUND_IMAGE, (GAME_AREA.x, GAME_AREA.y))
    Map.draw()
    Bomb.reDraw()
    BombWave.reDraw()
    player1.draw()
    pygame.display.update()


def main():
    Map.draw()
    running = True
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player1.bombCapacity > 0:  # DAT BOMB
                    player1.datBomb()

        for obj in CanWalkThrough:
            if ObjsList.get(obj):
                # print(distance(obj))
                if player1.distance(obj) > 49:
                    ObjsList[(obj)].canWalkThrough = False
                    CanWalkThrough.pop(CanWalkThrough.index(obj))
            else:
                CanWalkThrough.pop(CanWalkThrough.index(obj))

        if len(BombsList) > 0 and pygame.time.get_ticks() - BombsList[0].set_time > 3 * 1000:
            BitMap[BombsList[0].y][BombsList[0].x] = 0
            ObjsList.pop((BombsList[0].y, BombsList[0].x))
            player1.bombCapacity += 1
            ExploringBomb.append(BombsList.pop(0))

        player1.handle_movement(pygame.key.get_pressed())
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
