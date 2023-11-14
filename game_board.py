from sys import exit
import board_creator
import pygame

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
GREEN = (118,150,86)
WHITE = (255, 255, 255)

# initializing the board
Board = board_creator.reset_board()

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
                pygame.draw.rect(screen, GREEN, ((i*length)+offset,(j*length)+offset, length, length))
            else:
                pygame.draw.rect(screen, WHITE, ((i*length)+offset,(j*length)+offset, length, length))
            if Board[str(j) + str(i)]:
                screen.blit(Board[str(j) + str(i)], ((i*length)+2*offset,(j*length)+2*offset))
    pygame.display.update()
    clock.tick(60)