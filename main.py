
import sys
import pygame
from pygame import key
from pygame.constants import MOUSEBUTTONDOWN

from modules import Bomb, BombWave, Button, Colors, Item, Map, Player
from modules.Game_Config import *
start_time = 0


def player1_handle_movement(player1):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:  # MOVE LEFT
        player1.move_left()
    if keys_pressed[pygame.K_d]:  # MOVE RIGHT
        player1.move_right()
    if keys_pressed[pygame.K_w]:  # MOVE UP
        player1.move_up()
    if keys_pressed[pygame.K_s]:  # MOVE DOWN
        player1.move_down()


def player2_handle_movement(player2):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:  # MOVE LEFT
        player2.move_left()
    if keys_pressed[pygame.K_RIGHT]:  # MOVE RIGHT
        player2.move_right()
    if keys_pressed[pygame.K_UP]:  # MOVE UP
        player2.move_up()
    if keys_pressed[pygame.K_DOWN]:  # MOVE DOWN
        player2.move_down()


def draw_window(player1, player2):
    SCREEN.fill(Colors.BLUE)
    pygame.draw.rect(SCREEN, Colors.BLACK,
                     (GAME_AREA.x - 5, GAME_AREA.y - 5, GAME_AREA.width + 10, GAME_AREA.height + 10), border_radius=5)
    SCREEN.blit(BACKGROUND_IMAGE, (GAME_AREA.x, GAME_AREA.y))
    SCREEN.blit(PANEL_IMAGE, (S * 18, 0))
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

    # # FPS
    # current_fps = FONT.render(
    #     "FPS " + str(int(CLOCK.get_fps())), True, (0, 0, 0))
    # SCREEN.blit(current_fps, (0, 0))

    # Player1 Attributes
    player1_speed = FONT.render(str(player1.speed), True, (0, 0, 0))
    player1_capacity = FONT.render(str(player1.bombCapacity), True, (0, 0, 0))
    player1_strength = FONT.render(str(player1.bombLength), True, (0, 0, 0))
    SCREEN.blit(player1_capacity, (S * 23, S * 18 * 17 / 45))
    SCREEN.blit(player1_speed, (S * 23, S * 18 * 4 / 9))
    SCREEN.blit(player1_strength, (S * 23, S * 18 * 23 / 45))

    # Player2 Attributes
    player2_speed = FONT.render(str(player2.speed), True, (0, 0, 0))
    player2_capacity = FONT.render(str(player2.bombCapacity), True, (0, 0, 0))
    player2_strength = FONT.render(str(player2.bombLength), True, (0, 0, 0))
    SCREEN.blit(player2_capacity, (S * 23, S * 18 * 34 / 45))
    SCREEN.blit(player2_speed, (S * 23, S * 18 * 37 / 45))
    SCREEN.blit(player2_strength, (S * 23, S * 18 * 8 / 9))

    # Clock
    global start_time
    current_time = pygame.time.get_ticks() - start_time
    countDownClock = FONT.render(
        f"{(TIME-current_time)//60000}:{(TIME-current_time)%60000//1000}", True, (255, 255, 255))
    SCREEN.blit(countDownClock,
                (S * 22-countDownClock.get_rect().width/2, S * 2))
    if TIME - current_time <= 0:
        SCREEN.blit(DRAW_WIN, (0, 0))
        pygame.display.update()
        pygame.time.wait(3000)
        main()
    pygame.display.update()


def menu():
    running = True
    start_button = Button.Button(
        SCREEN.get_rect().centerx - S * 2.74 / 2, S * 16, "start")
    while running:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if start_button.isOver(mouse_pos):
                    main()
        SCREEN.blit(MENU_IMAGE, (0, 0))
        start_button.draw()
        pygame.display.update()
    pygame.quit()


def main():
    running = True

    # Reset game data
    BitMap.clear()
    BombsList.clear()
    ExploringBomb.clear()
    ObjsList.clear()
    ItemsList.clear()
    player1 = Player.Player(S + S / 2, S + S / 2, "Player 1", 1)
    player2 = Player.Player(S * 15 + S / 2, S * 15 + S / 2, "Player 2", 2)
    global start_time
    start_time = pygame.time.get_ticks()

    Map.load_map()
    Map.update_objects()
    while running:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Player 1 set Bomb
                    player1.set_Bomb()
                if event.key == pygame.K_SLASH:  # Player 2 set Bomb
                    player2.set_Bomb()
        player1.handleBomb()
        player1_handle_movement(player1)
        player1.collectItem()

        player2.handleBomb()
        player2_handle_movement(player2)
        player2.collectItem()

        draw_window(player1, player2)
        for bomb in ExploringBomb:
            for pos in bomb.wave.All:
                if player1.get_pos() == pos:
                    SCREEN.blit(P2_WIN, (0, 0))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    main()
                if player2.get_pos() == pos:
                    SCREEN.blit(P1_WIN, (0, 0))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    main()


if __name__ == "__main__":
    menu()
