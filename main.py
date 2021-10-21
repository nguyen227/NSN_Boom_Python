import pygame
from pygame import key
from pygame import math
import Colors
import Bomb
from Map import BITMAP
import Object
from Player import Player
import math

from pygame import mixer

# Initialize the pygame
pygame.init()

mixer.music.load('./data/sounds/soundMenu.wav')
mixer.music.play(-1)

WIDTH, HEIGHT = 1300, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NSN Boooooom")
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("./data/images/background1.jpg"), (850, 850))
FPS = 60
GAME_AREA = pygame.Rect(25, 25, 850, 850)
objects = {}
BombsList = []
player1 = Player(75, 75, 50, 50)


def draw_map():
    for i in range(len(BITMAP)):
        for j in range(len(BITMAP[i])):
            objects[(i, j)] = Object.Object(j, i)
            objects[(i, j)].draw()


def update_map():
    for object in objects.values():
        object.draw()


def draw_window():
    WIN.fill(Colors.BLUE)
    WIN.blit(BACKGROUND_IMAGE, (25, 25))
    update_map()
    player1.draw()
    for i in BombsList:
        i.redrawBomb()
    pygame.display.update()


def checkCollsion(dirx, diry):
    x = player1.box.x - 25
    y = player1.box.y - 25

    for i in range(player1.speed, 0, -1):
        x += dirx * i
        y += diry * i
        if y + 49 > 850 or x + 49 > 850 or y < 0 or x < 0:
            break
        if objects[(y//50, x//50)].coTheDiQua and objects[((y+49)//50, x//50)].coTheDiQua and objects[(y//50, (x+49)//50)].coTheDiQua and objects[((y+49)//50, (x+49)//50)].coTheDiQua:
            return i
    return 0


def player1_handle_movement(keys_pressed):
    # LEFT
    if keys_pressed[pygame.K_LEFT]:
        player1.box.x -= checkCollsion(-1, 0)
    # RIGHT
    if keys_pressed[pygame.K_RIGHT]:
        player1.box.x += checkCollsion(1, 0)
    # UP
    if keys_pressed[pygame.K_UP]:
        player1.box.y -= checkCollsion(0, -1)
    # DOWN
    if keys_pressed[pygame.K_DOWN]:
        player1.box.y += checkCollsion(0, 1)


def distant():
    x1, y1 = player1.box.x, player1.box.y
    x2, y2 = player1.previous_pos
    return math.sqrt((x1-x2*50.0 - 25)**2 + (y1 - y2*50.0 - 25)**2)


def main():  # Gameloop
    clock = pygame.time.Clock()
    running = True
    vuadatbomb = False
    draw_map()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player1.bombCapacity > 0:  # DAT BOMB
                    vuadatbomb = True
                    player1.bombCapacity -= 1
                    BombsList.append(
                        Bomb.Bomb(player1.box.x, player1.box.y, pygame.time.get_ticks()))
                    BombsList[-1].redrawBomb()
                    player1.set_previous_pos()
                    BITMAP[BombsList[-1].y][BombsList[-1].x] = 10

        if(vuadatbomb and distant() >= 49):
            if len(BombsList) > 0:
                objects[(BombsList[-1].y, BombsList[-1].x)].coTheDiQua = False
            vuadatbomb = False
        if len(BombsList) > 0 and pygame.time.get_ticks() - BombsList[0].set_time > 3 * 1000:
            BITMAP[BombsList[0].y][BombsList[0].x] = 0
            objects[(BombsList[0].y, BombsList[0].x)].coTheDiQua = True
            BombsList[0].drawBombWave()
            BombsList.pop(0)
            player1.bombCapacity += 1
        keys_pressed = pygame.key.get_pressed()
        player1_handle_movement(keys_pressed)
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
