import pygame

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
    pawn_white = pygame.image.load('ChessPieces/pawn_white.png')
    pawn_black = pygame.image.load('ChessPieces/pawn_black.png')
    for i in range(8):
        Board["6"+str(i)] = pawn_white
        Board["1"+str(i)] = pawn_black

    # Creating rooks
    rook_black = pygame.image.load('ChessPieces/rook_black.png')
    rook_white = pygame.image.load('ChessPieces/rook_white.png')
    Board["70"]= rook_white
    Board["77"]= rook_white
    Board["00"]= rook_black
    Board["07"]= rook_black

    # Creating queen
    queen_black = pygame.image.load('ChessPieces/queen_black.png')
    queen_white = pygame.image.load('ChessPieces/queen_white.png')
    Board["74"]= queen_white
    Board["04"]= queen_black

    # creating kings
    king_black = pygame.image.load('ChessPieces/king_black.png')
    king_white = pygame.image.load('ChessPieces/king_white.png')
    Board["73"]= king_white
    Board["03"]= king_black

    # creating camels
    camel_black = pygame.image.load('ChessPieces/camel_black.png')
    camel_white = pygame.image.load('ChessPieces/camel_white.png')
    Board["72"]= camel_white
    Board["75"]= camel_white
    Board["02"]= camel_black
    Board["05"]= camel_black

    # creating knights
    knight_black = pygame.image.load('ChessPieces/knight_black.png')
    knight_white = pygame.image.load('ChessPieces/knight_white.png')
    Board["71"]= knight_white
    Board["76"]= knight_white
    Board["01"]= knight_black
    Board["06"]= knight_black
    return Board
