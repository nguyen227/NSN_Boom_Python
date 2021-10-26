
import pygame
from pygame import key

from modules import Bomb, BombWave, Colors, Map, Player, Item
from modules.Game_Config import *

player1 = Player.Player(75, 75)


def draw_window():
    SCREEN.fill(Colors.BLUE)
    SCREEN.blit(BACKGROUND_IMAGE, (GAME_AREA.x, GAME_AREA.y))
    Map.draw()
    Bomb.reDraw()
    player1.draw()
    Item.draw()
    BombWave.reDraw()
    pygame.display.update()


def main():
    # Map.draw()
    running = True
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Set Bomb
                    player1.set_Bomb()
        player1.handleBomb()
        player1.handle_movement()
        player1.handle_item()
        print(player1.speed, player1.bombCapacity, player1.bombLength)
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
