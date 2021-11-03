
import pygame
from pygame import key

from modules import Bomb, BombWave, Colors, Map, Player, Item
from modules.Game_Config import *

player1 = Player.Player(75, 75, "Player 1")
player2 = Player.Player(775, 775, "Player 2")


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
    if keys_pressed[pygame.K_UP]:  # MOVE UP
        player2.move_up()
    if keys_pressed[pygame.K_DOWN]:  # MOVE DOWN
        player2.move_down()


def draw_window():
    SCREEN.fill(Colors.BLUE)
    pygame.draw.rect(SCREEN, Colors.BLACK, (GAME_AREA.x-5,
                     GAME_AREA.y-5, GAME_AREA.width + 10, GAME_AREA.height+10), border_radius=5)
    SCREEN.blit(BACKGROUND_IMAGE, (GAME_AREA.x, GAME_AREA.y))
    SCREEN.blit(PANEL_IMAGE, (900, 0))
    BombWave.reDraw()
    for i in range(17):
        for j in range(17):
            if BombsList.get((i, j)):
                BombsList[(i, j)].animations()
            if ItemsList.get((i, j)):
                ItemsList[(i, j)].draw()
            if ObjsList.get((i, j)):
                ObjsList[(i, j)].draw()
            if player1.get_pos() == (i, j):
                player1.draw()
            if player2.get_pos() == (i, j):
                player2.draw()

    # FPS
    current_fps = FONT.render(
        "FPS " + str(int(CLOCK.get_fps())), True, (0, 0, 0))
    SCREEN.blit(current_fps, (0, 0))

    player1_speed = FONT.render(str(player1.speed), True, (0, 0, 0))
    player1_capacity = FONT.render(str(player1.bombCapacity), True, (0, 0, 0))
    player1_strenght = FONT.render(str(player1.bombLength), True, (0, 0, 0))
    SCREEN.blit(player1_capacity, (1150, 340))
    SCREEN.blit(player1_speed, (1150, 400))
    SCREEN.blit(player1_strenght, (1150, 460))

    player2_speed = FONT.render(str(player2.speed), True, (0, 0, 0))
    player2_capacity = FONT.render(str(player2.bombCapacity), True, (0, 0, 0))
    player2_strenght = FONT.render(str(player2.bombLength), True, (0, 0, 0))
    SCREEN.blit(player2_capacity, (1150, 680))
    SCREEN.blit(player2_speed, (1150, 740))
    SCREEN.blit(player2_strenght, (1150, 800))

    pygame.display.update()


def main():
    running = True
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Player 1 set Bomb
                    player1.set_Bomb()
                if event.key == pygame.K_SLASH:  # Player 2 set Bomb
                    player2.set_Bomb()
        player1.handleBomb()
        player1_handle_movement()
        player1.collectItem()

        player2.handleBomb()
        player2_handle_movement()
        player2.collectItem()

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
