import pygame
from pygame import key

from Player import Player
from Bomb import Bomb
# Initialize the pygame
pygame.init()

# Create the screen
WIDTH, HEIGHT = 1300, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set captions
pygame.display.set_caption("NSN Boooooom")


GAMEAREA = pygame.Rect(25, 25, 850, 850)
IMAGES = [(pygame.image.load("./data/images/0.png")),
          (pygame.transform.scale(pygame.image.load("./data/images/1.png"), (50, 71))),
          (pygame.image.load("./data/images/2.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/4.png")),
          (pygame.image.load("./data/images/5.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/3.png")),
          (pygame.image.load("./data/images/boom1.png"))]
CHARACTER_IMAGE = pygame.image.load("./data/images/player_down_1.png")

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("./data/images/background1.jpg"), (900, 900))
WHITE = (255, 255, 255)
FPS = 60

# Read map data
BITMAP = []
file = open("./data/maps/level2.txt", "r")
map = file.readlines()
for i in range(len(map)):
    BITMAP.append([int(x) for x in map[i].split()])
file.close()


def draw_map(objects):
    for i in range(len(BITMAP)):
        for j in range(len(BITMAP[i])):
            if BITMAP[i][j] != 0 and BITMAP[i][j] != 10:
                objects.append(pygame.Rect(
                    GAMEAREA.x + j*50, GAMEAREA.y + i*50, 50, 50))
            WIN.blit(IMAGES[BITMAP[i][j]],
                     (GAMEAREA.x + j*50, GAMEAREA.y + i*50))


def draw_window(player1, objects):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    draw_map(objects)
    player1.draw()
    pygame.display.update()


def player1_handle_movement(keys_pressed, player1, objects):
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        player1.playerRect.x -= player1.speed
        for object in objects:
            if player1.playerRect.colliderect(object):
                player1.playerRect.x += player1.speed
                break
        if player1.playerRect.x < GAMEAREA.x:
            player1.playerRect.x = GAMEAREA.x
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        player1.playerRect.x += player1.speed
        for object in objects:
            if player1.playerRect.colliderect(object):
                player1.playerRect.x -= player1.speed
                break
        if player1.playerRect.x > 875 - player1.width:
            player1.playerRect.x = 875 - player1.width
    if keys_pressed[pygame.K_UP]:  # UP
        player1.playerRect.y -= player1.speed
        for object in objects:
            if player1.playerRect.colliderect(object):
                player1.playerRect.y += player1.speed
                break
        if player1.playerRect.y < GAMEAREA.y:
            player1.playerRect.y = GAMEAREA.y
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        player1.playerRect.y += player1.speed
        for object in objects:
            if player1.playerRect.colliderect(object):
                player1.playerRect.y -= player1.speed
                break
        if player1.playerRect.y > 875 - player1.width:
            player1.playerRect.y = 875 - player1.width


def main():  # Gameloop
    player1 = Player(75, 75, 50, 50, WIN)
    objects = []
    BombsList = []
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # DAT BOMB
                    BombsList.append(Bomb(
                        ((player1.playerRect.x) // 50), ((player1.playerRect.y) // 50), pygame.time.get_ticks(), WIN))
                    BITMAP[((player1.playerRect.y) // 50)
                           ][((player1.playerRect.x) // 50)] = 10
        if len(BombsList) > 0 and pygame.time.get_ticks() - BombsList[0].time_set > 3 * 1000:
            BITMAP[BombsList[0].y][BombsList[0].x] = 0
            BombsList[0].drawBombWave()
            BombsList.pop(0)

        keys_pressed = pygame.key.get_pressed()
        player1_handle_movement(keys_pressed, player1, objects)
        draw_window(player1, objects)
    pygame.quit()


if __name__ == "__main__":
    main()
