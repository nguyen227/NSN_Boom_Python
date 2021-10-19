import pygame
from pygame import key
# Initialize the pygame
pygame.init()

# Create the screen
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set captions
pygame.display.set_caption("NSN Boooooom")


def player():  # Player
    pass


SPEED = 5
CHARACTER_IMAGE = pygame.image.load("./data/images/player_down_1.png")
STONE_IMAGE = pygame.transform.scale(
    pygame.image.load("./data/images/da1.png"), (50, 50))

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("./data/images/background1.jpg"), (900, 900))
WHITE = (255, 255, 255)
FPS = 60

# Read map data
BITMAP = []
file = open("./data/maps/level1.txt", "r")
map = file.readlines()
for i in range(len(map)):
    BITMAP.append([int(x) for x in map[i].split()])
file.close()


def draw_map():
    for i in range(len(BITMAP)):
        for j in range(len(BITMAP[i])):
            if BITMAP[i][j] >= 1:
                WIN.blit(STONE_IMAGE, (j*50, i*50))


def draw_window(character):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    draw_map()
    WIN.blit(CHARACTER_IMAGE, (character.x, character.y))
    pygame.display.update()


def character_handle_movement(keys_pressed, character):
    if keys_pressed[pygame.K_LEFT] and character.x >= 0:  # LEFT
        character.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and character.x <= 600:  # RIGHT
        character.x += SPEED
    if keys_pressed[pygame.K_UP] and character.y >= 0:  # UP
        character.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and character.y <= 600:  # DOWN
        character.y += SPEED


def main():  # Gameloop
    character = pygame.Rect(0, 0, 45, 65)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys_pressed = pygame.key.get_pressed()
        character_handle_movement(keys_pressed, character)
        draw_window(character)
    pygame.quit()


if __name__ == "__main__":
    main()
