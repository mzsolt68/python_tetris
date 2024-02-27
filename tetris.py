''' Simple Tetris game using Pygame. '''

import time
import sys
import pygame as pg
from piece import Piece
from board import GameBoard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

def position_valid(board: GameBoard, piece: Piece, adj_row=0, adj_column=0):
    ''' Check, if the position of the piece is valid. '''
    shape_matrix = piece.shape[piece.rotation]
    for row in range(5):
        for column in range(5):
            if shape_matrix[row][column] == '.':
                continue
            if not is_on_board(piece.row + row + adj_row, piece.column + column + adj_column):
                return False
            if board.board[row + piece.row + adj_row][column + piece.column + adj_column] != '.':
                return False
    return True

def check_keypress(board: GameBoard, piece: Piece):
    ''' Check, if user pressed a key. '''
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and \
                position_valid(board, piece, adj_column=-1):
                piece.move_left()
            elif event.key == pg.K_RIGHT and \
                position_valid(board, piece, adj_column=1):
                piece.move_right()
            elif event.key == pg.K_UP:
                piece.rotate()
                if not position_valid(board, piece):
                    piece.rotate_back()

def is_on_board(row, column):
    ''' Check, if the position is on the board. '''
    return 0 <= column < BOARD_WIDTH and row < BOARD_HEIGHT

def game():
    ''' Main game loop. '''
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('Tetris')
    game_board = GameBoard(screen, BOARD_WIDTH, BOARD_HEIGHT)
    piece = Piece()
    last_move = time.time()
    #clock = pg.time.Clock()
    score = 0
    while True:
        screen.fill((BLACK))

        if time.time() - last_move > 0.5:
            piece.move_down()
            last_move = time.time()

        game_board.draw_frame()
        game_board.draw_shape(piece)

        game_board.draw()
        game_board.print_score()
        check_keypress(game_board, piece)

        if not position_valid(game_board, piece, adj_row=1):
            game_board.update(piece)
            game_board.remove_complete_lines()
            piece = Piece()

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        #clock.tick(10)

if __name__ == '__main__':
    game()
