import pygame
from pieces import *

def reset_board():
    """
    This function reset or create new board for the chess game
    """
    Board = {}
    # Creating Board
    for i in range(8):
        for j in range(8):
            Board[str(j) + str(i)] = None
    # Creating Pawns
    for i in range(8):
        Board["6"+str(i)] = pawn_white
        Board["1"+str(i)] = pawn_black

    # Creating rooks
    Board["70"]= rook_white
    Board["77"]= rook_white
    Board["00"]= rook_black
    Board["07"]= rook_black

    # Creating queen
    Board["74"]= queen_white
    Board["04"]= queen_black

    # creating kings
    Board["73"]= king_white
    Board["03"]= king_black

    # creating camels
    Board["72"]= camel_white
    Board["75"]= camel_white
    Board["02"]= camel_black
    Board["05"]= camel_black

    # creating knights
    Board["71"]= knight_white
    Board["76"]= knight_white
    Board["01"]= knight_black
    Board["06"]= knight_black
    return Board
