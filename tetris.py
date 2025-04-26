''' Simple Tetris game using Pygame. '''

import time
import sys
import pygame as pg
from piece import Piece
from board import GameBoard
import gamecolors as colors

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

def check_keypress(board: GameBoard, piece: Piece):
    ''' Check, if user pressed a key. '''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and \
                board.is_position_valid(piece, adj_column=-1):
                piece.move_left()
            elif event.key == pg.K_RIGHT and \
                board.is_position_valid(piece, adj_column=1):
                piece.move_right()
            elif event.key == pg.K_UP:
                piece.rotate()
                if not board.is_position_valid(piece):
                    piece.rotate_back()
            elif event.key == pg.K_DOWN:
                piece.drop_speed = 0.03
        elif event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                piece.drop_speed = 0.5  # Reset drop speed when key is released
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

def game():
    ''' Main game loop. '''
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('Tetris')
    clock = pg.time.Clock()
    game_board = GameBoard(screen, BOARD_WIDTH, BOARD_HEIGHT)
    piece = Piece()
    last_move = time.time()

    # Enable key repeat functionality
    pg.key.set_repeat(200, 50)  # 200ms delay, 50ms interval

    while True:
        screen.fill(colors.BLACK)

        # Limit frame rate to 30 FPS
        clock.tick(30)

        # Handle events
        check_keypress(game_board, piece)

        # Move piece down based on drop speed
        if time.time() - last_move > piece.drop_speed:
            piece.move_down()
            last_move = time.time()

        # Draw only the necessary parts
        game_board.draw_frame()
        game_board.draw_shape(piece)
        game_board.draw()
        game_board.print_score()

        # Check if the piece has landed
        if not game_board.is_position_valid(piece, adj_row=1):
            game_board.update(piece)
            game_board.remove_complete_lines()
            piece = Piece()

        # Update the display
        pg.display.flip()  

if __name__ == '__main__':
    game()
