from sys import exit
import board_creator
import pygame
import time
from pieces import *

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
white_king = "73"
black_king = "03"
selected = None
turn = True

# creating clock object
clock = pygame.time.Clock()


# running the game
while True:
    for event in pygame.event.get():
        # quitting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # checking for moves
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            x, y = pygame.mouse.get_pos()
            x_pos = (x-offset)//(length)
            y_pos = (y-offset)//(length)
            clicked = str(y_pos) + str(x_pos)

            # checking if the position is valid
            if y_pos > 7 or y_pos<0 or x_pos<0 or x_pos > 7:
                selected = None

            # checking if selected
            elif not selected:
                print(turn, turn and Board[clicked] in team["white"], not turn, Board[clicked] in team["black"])
                if turn and Board[clicked] in team["white"]:
                    selected = str(y_pos) + str(x_pos)
                elif not turn and Board[clicked] in team["black"]:
                    selected = str(y_pos) + str(x_pos)

            # checking if not selected
            else:        
                Board[clicked], Board[selected] = Board[selected], None
                selected = None
                turn = not turn
    flag = True
    for i in range(8):
        flag = not flag
        for j in range(8):
            flag = not flag
            if flag:
                pygame.draw.rect(screen, GREEN, ((i*length)+offset,(j*length)+offset, length, length))
            else:
                pygame.draw.rect(screen, WHITE, ((i*length)+offset,(j*length)+offset, length, length))
            if selected == str(j) + str(i):
                    pygame.draw.rect(screen, pygame.Color((173, 216, 230, 128)), ((i*length)+offset,(j*length)+offset, length, length))
            if Board[str(j) + str(i)]:
                screen.blit(Board[str(j) + str(i)], ((i*length)+2*offset,(j*length)+2*offset))
    pygame.display.update()
    clock.tick(60)