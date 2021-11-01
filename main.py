
import pygame
from pygame import key

from modules import Bomb, BombWave, Colors, Map, Player, Item
from modules.Game_Config import *

# <<<<<<< HEAD

# player1 = Player.Player(75, 75)
# player2 = Player.Player(75, 75)
# =======
player1 = Player.Player(75, 75, "Player 1")
player2 = Player.Player(775, 775, "Player 2")
# >>>>>>> 2f31d96a0ee9c96a2d6d2f9d2f2749c08109204a


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
    SCREEN.blit(BACKGROUND_IMAGE, (GAME_AREA.x, GAME_AREA.y))
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
    BombWave.reDraw()

    # FPS
    current_fps = FONT.render(
        "FPS " + str(int(CLOCK.get_fps())), True, (0, 0, 0))
    SCREEN.blit(current_fps, (0, 0))

    player_speed = FONT.render("SPEED " + str(player1.speed), True, (0, 0, 0))
    player_capacity = FONT.render(
        "CAPACITY " + str(player1.bombCapacity), True, (0, 0, 0))
    player_strenght = FONT.render(
        "STRENGHT " + str(player1.bombLength), True, (0, 0, 0))
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
    running = True
    while running:
        # CLOCK.tick(FPS)
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
        player1.handle_item()

        player2.handleBomb()
        player2_handle_movement()
        player2.handle_item()

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
