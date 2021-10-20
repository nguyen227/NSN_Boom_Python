import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
    current_time = pygame.time.get_ticks()
    print(clock.get_time())
    pygame.display.flip()
    clock.tick(60)
