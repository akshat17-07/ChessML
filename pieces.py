"""
This file define all pieces in the game
"""
import pygame

# pawns   
pawn_white = pygame.image.load('ChessPieces/pawn_white.png')
pawn_black = pygame.image.load('ChessPieces/pawn_black.png')

# rooks
rook_black = pygame.image.load('ChessPieces/rook_black.png')
rook_white = pygame.image.load('ChessPieces/rook_white.png')


# queens
queen_black = pygame.image.load('ChessPieces/queen_black.png')
queen_white = pygame.image.load('ChessPieces/queen_white.png')
    
# kings
king_black = pygame.image.load('ChessPieces/king_black.png')
king_white = pygame.image.load('ChessPieces/king_white.png')

# camels
camel_black = pygame.image.load('ChessPieces/camel_black.png')
camel_white = pygame.image.load('ChessPieces/camel_white.png')

# knights=     
knight_black = pygame.image.load('ChessPieces/knight_black.png')
knight_white = pygame.image.load('ChessPieces/knight_white.png')

team = {"white": set([rook_white, camel_white, knight_white, pawn_white, queen_white]), 
        "black": set([rook_black, camel_black, knight_black, pawn_black, queen_black])}