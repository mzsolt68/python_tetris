''' Simple Tetris game using Pygame. '''

import time
import sys
import pygame as pg
from piece import Piece
from board import GameBoard

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOX_SIZE = 20
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
                piece.column -= 1
            elif event.key == pg.K_RIGHT and \
                position_valid(board, piece, adj_column=1):
                piece.column += 1
            elif event.key == pg.K_UP:
                piece.rotation = (piece.rotation + 1) % len(piece.shape)
                if not position_valid(board, piece):
                    piece.rotation = (piece.rotation - 1) % len(piece.shape)

def is_on_board(row, column):
    ''' Check, if the position is on the board. '''
    return 0 <= column < BOARD_WIDTH and row < BOARD_HEIGHT

def print_score(screen, score):
    ''' Print the score on the screen. '''
    font = pg.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (250, 10))

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
            piece.row += 1
            last_move = time.time()

        game_board.draw_frame()
        game_board.draw_shape(piece)

        game_board.draw()
        print_score(screen, score)
        check_keypress(game_board, piece)

        if not position_valid(game_board, piece, adj_row=1):
            game_board.update(piece)
            removed_lines = game_board.remove_complete_lines()
            score += removed_lines
            piece = Piece()

        pg.display.update()
        for _ in pg.event.get(pg.QUIT):
            pg.quit()
            sys.exit()

        #clock.tick(10)

if __name__ == '__main__':
    game()
