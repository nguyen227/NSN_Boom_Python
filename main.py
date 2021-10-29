
import pygame
from pygame import key

from modules import Bomb, BombWave, Colors, Map, Player, Item
from modules.Game_Config import *

player1 = Player.Player(75, 75)
player2 = Player.Player(75, 75)


def player1_handle_movement():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:  # MOVE LEFT
        player1.move_left()
    if keys_pressed[pygame.K_d]:  # MOVE RIGHT
        player1.move_right()
    if keys_pressed[pygame.K_w]:  # MOVE UP
        player1.move_up()
    if keys_pressed[pygame.K_s]:  # MOVE DOWN
        player1.move_down()


def player2_handle_movement():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:  # MOVE LEFT
        player2.move_left()
    if keys_pressed[pygame.K_RIGHT]:  # MOVE RIGHT
        player2.move_right()
    if keys_pressed[pygame.K_UP]:  # MOVE UPôi
        player2.move_up()
    if keys_pressed[pygame.K_DOWN]:  # MOVE DOWN
        player2.move_down()


def draw_window():
    SCREEN.fill(Colors.BLUE)
    SCREEN.blit(BACKGROUND_IMAGE, (GAME_AREA.x, GAME_AREA.y))
    Map.draw()
    Bomb.reDraw()
    player1.draw()
    player2.draw()
    Item.draw()
    BombWave.reDraw()

    # FPS
    current_fps = FONT.render(
        "FPS " + str(int(CLOCK.get_fps())), True, (0, 0, 0))

    player_speed = FONT.render("SPEED " + str(player1.speed), True, (0, 0, 0))
    player_capacity = FONT.render(
        "CAPACITY " + str(player1.bombCapacity), True, (0, 0, 0))
    player_strenght = FONT.render(
        "STRENGHT " + str(player1.bombLength), True, (0, 0, 0))
    SCREEN.blit(current_fps, (0, 0))
    SCREEN.blit(player_speed, (900, 25))
    SCREEN.blit(player_capacity, (1000, 25))
    SCREEN.blit(player_strenght, (1150, 25))

    player_speed = FONT.render("SPEED " + str(player2.speed), True, (0, 0, 0))
    player_capacity = FONT.render(
        "CAPACITY " + str(player2.bombCapacity), True, (0, 0, 0))
    player_strenght = FONT.render(
        "STRENGHT " + str(player2.bombLength), True, (0, 0, 0))
    SCREEN.blit(player_speed, (900, 50))
    SCREEN.blit(player_capacity, (1000, 50))
    SCREEN.blit(player_strenght, (1150, 50))

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
                if event.key == pygame.K_SLASH:
                    player2.set_Bomb()
        player1.handleBomb()
        player1_handle_movement()
        player1.handle_item()

        player2.handleBomb()
        player2_handle_movement()
        player2.handle_item()
        # print(player1.speed, player1.bombCapacity, player1.bombLength)
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
