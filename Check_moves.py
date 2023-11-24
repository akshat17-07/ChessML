import pygame
import pieces
def valid_move(Board, move, turn):
    team_alt = list(pieces.team.values())
    if turn:
        if Board[move[1]] in team_alt[0]:
            return False
        # white to move
        # False if move[1] of team white
    else:
        if Board[move[1]] in team_alt[1]:
            return False
        # black to move
        # False if move[1] of team black
    if move[0] == move[1]:
        # Click on same space
        return False
    
    return True
