import pygame
from pygame import key
from pygame import math
from Game_Config import *

import Colors
import Bomb
import Map
import Object
import Player
import math

player1 = Player.Player(75, 75, 50, 50)


def draw_window():
    SCREEN.fill(Colors.BLUE)
    SCREEN.blit(BACKGROUND_IMAGE, (25, 25))
    Map.draw()
    player1.draw()
    for i in BombsList:
        i.redrawBomb()
    for i in BombExplored:
        if pygame.time.get_ticks() - i.explore_time <= 1.5 * 1000:
            i.drawBombWave()
    pygame.display.update()


def distant():
    x1, y1 = player1.box.x, player1.box.y
    x2, y2 = player1.previous_pos
    return math.sqrt((x1-x2*50.0 - 25)**2 + (y1 - y2*50.0 - 25)**2)


def main():
    Map.draw()
    clock = pygame.time.Clock()
    running = True
    vuadatbomb = False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player1.bombCapacity > 0:  # DAT BOMB
                    if Map.BITMAP[(player1.box.y-25)//50][(player1.box.x - 25)//50] == 0:
                        vuadatbomb = True
                        player1.bombCapacity -= 1
                        BombsList.append(
                            Bomb.Bomb(player1.box.x-25, player1.box.y-25, pygame.time.get_ticks()))
                        # BombsList[-1].redrawBomb()
                        player1.set_previous_pos()
                        Map.BITMAP[BombsList[-1].y][BombsList[-1].x] = 10

        if(vuadatbomb and distant() > 49):
            if len(BombsList) > 0:
                # print(BombsList[-1].y, BombsList[-1].x)
                if objects.get((BombsList[-1].y, BombsList[-1].x)):
                    objects[(BombsList[-1].y, BombsList[-1].x)
                            ].coTheDiQua = False
            vuadatbomb = False
        if len(BombsList) > 0 and pygame.time.get_ticks() - BombsList[0].set_time > 3 * 1000:
            Map.BITMAP[BombsList[0].y][BombsList[0].x] = 0
            objects[(BombsList[0].y, BombsList[0].x)].coTheDiQua = True
            player1.bombCapacity += 1
            BombExplored.append(BombsList.pop(0))
        keys_pressed = pygame.key.get_pressed()
        player1.handle_movement(keys_pressed)
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
