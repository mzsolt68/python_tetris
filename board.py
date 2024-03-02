''' This module contains the GameBoard class. '''

from pygame import Surface, draw, font
from piece import Piece
import gamecolors as colors

BOX_SIZE = 20

class Cell:
    ''' Class to reperesent a single cell of the board.'''
    def __init__(self, state: str, color: tuple):
        self.state = state
        self.color = color

class GameBoard:
    ''' A class to represent the game board. '''
    def __init__(self, screen: Surface, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [[Cell('.', ()) for _ in range(self.width)] for _ in range(self.height)]
        self.screen = screen
        self.score = 0
        self.font = font.Font(None, 36)

    def update(self, piece: Piece):
        ''' Update the board with the piece. '''
        for row in range(5):
            for column in range(5):
                if piece.shape[piece.rotation][row][column] == 'x':
                    self.board[piece.row + row][piece.column + column].state = 'x'
                    self.board[piece.row + row][piece.column + column].color = piece.color

    def is_line_complete(self, row) -> bool:
        ''' Check, if the line is complete '''
        for column in range(self.width):
            if self.board[row][column].state == '.':
                return False
        return True

    def remove_line(self, row):
        ''' Remove the line from the board. '''
        del self.board[row]
        self.board.insert(0, [Cell('.', ()) for _ in range(self.width)])

    def remove_complete_lines(self):
        ''' Remove all complete lines from the board. '''
        lines_removed = 0
        for row in range(self.height):
            if self.is_line_complete(row):
                self.remove_line(row)
                lines_removed += 1
        self.score += lines_removed

    def draw(self):
        ''' Draw the board on the screen. '''
        for row in range(self.height):
            for column in range(self.width):
                if self.board[row][column].state == 'x':
                    self.draw_a_box(row, column, self.board[row][column].color, colors.GREY)

    def draw_a_box(self, row: int, column: int, color: tuple, border_color: tuple):
        ''' Draw a single box on the screen. '''
        x = 100 + 5 + (column * BOX_SIZE + 1)
        y = 50 + 5 + (row * BOX_SIZE + 1)
        draw.rect(self.screen, border_color, [x, y, BOX_SIZE, BOX_SIZE])
        draw.rect(self.screen, color, [x, y, BOX_SIZE - 2, BOX_SIZE - 2])

    def draw_shape(self, piece: Piece):
        ''' Draw the piece on the screen. '''
        shape_to_draw = piece.shape[piece.rotation]
        for row in range(5):
            for column in range(5):
                if shape_to_draw[row][column] == 'x':
                    self.draw_a_box(piece.row + row, piece.column + column, piece.color, colors.GREY)

    def draw_frame(self):
        ''' Draw the frame on the screen. '''
        draw.rect(self.screen, colors.BLUE, [100, 50, self.width * BOX_SIZE + 10, self.height * BOX_SIZE + 10], 5)

    def print_score(self):
        ''' Print the score on the screen. '''
        text = self.font.render("Score: " + str(self.score), True, colors.WHITE)
        self.screen.blit(text, (250, 10))