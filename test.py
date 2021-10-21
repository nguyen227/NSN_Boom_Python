import pygame
import sys

B_IMAGES = [(pygame.image.load("./data/images/boom1.png")),
            (pygame.image.load("./data/images/boom2.png")),
            (pygame.image.load("./data/images/boom3.png")),
            (pygame.image.load("./data/images/boom4.png")),
            (pygame.image.load("./data/images/boom5.png")),
            (pygame.image.load("./data/images/boom6.png")),
            (pygame.image.load("./data/images/boom7.png")),
            (pygame.image.load("./data/images/boom8.png"))]


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.current_sprite = 0
        self.image = B_IMAGES[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 0.2
        if self.current_sprite >= len(B_IMAGES):
            self.current_sprite = 0
        self.image = B_IMAGES[int(self.current_sprite)]


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1080, 720))

moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    screen.fill((255, 255, 255))
    moving_sprites.draw(screen)
    moving_sprites.update()
    clock.tick(60)
