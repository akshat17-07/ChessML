import pygame
from sys import exit

# initializing pygame settings
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Chess")

# creating clock object
clock = pygame.time.Clock()

# running the game
while True:

    for event in pygame.event.get():
        # quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)