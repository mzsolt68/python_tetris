''' This module contains the GameBoard class. '''

from piece import Piece

class GameBoard:
    ''' A class to represent the game board. '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['.' for _ in range(self.width)] for _ in range(self.height)]

    def update(self, piece: Piece):
        ''' Update the board with the piece. '''
        for row in range(5):
            for column in range(5):
                if piece.shape[piece.rotation][row][column] == 'x':
                    self.board[piece.row + row][piece.column + column] = 'x'