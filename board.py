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

    def is_line_complete(self, row):
        ''' Check, if the line is complete '''
        for column in range(self.width):
            if self.board[row][column] == '.':
                return False
        return True

    def remove_line(self, row):
        ''' Remove the line from the board. '''
        del self.board[row]
        self.board.insert(0, ['.'] * self.width)

    def remove_complete_lines(self) -> int:
        ''' Remove all complete lines from the board. '''
        lines_removed = 0
        for row in range(self.height):
            if self.is_line_complete(row):
                self.remove_line(row)
                lines_removed += 1
        return lines_removed