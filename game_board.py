import pygame
from sys import exit

# initializing pygame settings
pygame.init()
board_size = (1200, 800)
screen = pygame.display.set_mode(board_size)
pygame.display.set_caption("Chess")
screen.fill("grey")

# creating surface for white and black squares
offset = int(min(board_size[0]/90/8, board_size[1]/90/8)) + 20
length = int(min(board_size[0]/8 - board_size[0]/90/8,board_size[1]/8 - board_size[1]/90/8))
block_size = pygame.Surface((length, length))
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)


# creating clock object
clock = pygame.time.Clock()

# running the game
while True:

    for event in pygame.event.get():
        # quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    flag = True
    for i in range(8):
        flag = not flag
        for j in range(8):
            flag = not flag
            if flag:
                pygame.draw.rect(screen, WHITE, ((i*length)+offset,(j*length)+offset, length, length))
            else:
                pygame.draw.rect(screen, BLACK, ((i*length)+offset,(j*length)+offset, length, length))
            
    pygame.display.update()
    clock.tick(60)