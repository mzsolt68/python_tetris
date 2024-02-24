''' Simple Tetris game using Pygame. '''

import time
import sys
import random
import pygame as pg
from shapes import SHAPES

BLUE = (0, 0, 155)
WHITE = (255, 255, 255)
GREY = (217, 222, 226)
BOX_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

def create_board():
    ''' Create a 10x20 board with all empty spaces. '''
    board_columns = 10
    board_rows = 20
    board = []
    for _ in range(board_rows):
        new_row = []
        for _ in range(board_columns):
            new_row.append('.')
        board.append(new_row)
    return board

def create_piece():
    ''' Create a new piece at the top of the board. '''
    piece = {}
    piece['rotation'] = 0
    piece['shape'] = random.choice(list(SHAPES.keys()))
    piece['row'] = 0
    piece['column'] = 2
    return piece

def draw_a_box(screen, row, column, color, border_color):
    ''' Draw a box on the screen. '''
    origin_x = 100 + 5 + (column * BOX_SIZE + 1)
    origin_y = 50 + 5 + (row * BOX_SIZE + 1)
    pg.draw.rect(screen, border_color, [origin_x, origin_y, BOX_SIZE, BOX_SIZE])
    pg.draw.rect(screen, color, [origin_x, origin_y, BOX_SIZE - 2, BOX_SIZE - 2])

def draw_shape(screen, piece):
    ''' Draw the piece on the screen. '''
    shape_to_draw = SHAPES[piece['shape']][piece['rotation']]
    for row in range(5):
        for column in range(5):
            if shape_to_draw[row][column] == 'x':
                draw_a_box(screen, piece['row'] + row, piece['column'] + column, WHITE, GREY)

def update_board(board, piece):
    ''' Update the board with the piece. '''
    for row in range(5):
        for column in range(5):
            if SHAPES[piece['shape']][piece['rotation']][row][column] == 'x':
                board[piece['row'] + row][piece['column'] + column] = 'x'
    return board

def draw_board(screen, board):
    ''' Draw the actual board on the screen. '''
    for row in range(BOARD_HEIGHT):
        for column in range(BOARD_WIDTH):
            if board[row][column] == 'x':
                draw_a_box(screen, row, column, WHITE, GREY)

def position_valid(board, piece, adj_row=0, adj_column=0):
    ''' Check, if the position of the piece is valid. '''
    shape_matrix = SHAPES[piece['shape']][piece['rotation']]
    for row in range(5):
        for column in range(5):
            if shape_matrix[row][column] == '.':
                continue
            if not is_on_board(piece['row'] + row + adj_row, piece['column'] + column + adj_column):
                return False
            if board[row + piece['row'] + adj_row][column + piece['column'] + adj_column] != '.':
                return False
    # if not(0 <= column < BOARD_WIDTH and row < BOARD_HEIGHT):
    #     return False
    # if board[row][column] != '.':
    #     return False
    return True

def check_keypress(board, piece):
    ''' Check, if user pressed a key. '''
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and \
                position_valid(board, piece, adj_column=-1):
                piece['column'] -= 1
            elif event.key == pg.K_RIGHT and \
                position_valid(board, piece, adj_column=1):
                piece['column'] += 1
            elif event.key == pg.K_UP:
                piece['rotation'] = (piece['rotation'] + 1) % len(SHAPES[piece['shape']])
                if not position_valid(board, piece):
                    piece['rotation'] = (piece['rotation'] - 1) % len(SHAPES[piece['shape']])

def is_line_complete(board, row):
    ''' Check, if the line is complete '''
    for column in range(BOARD_WIDTH):
        if board[row][column] == '.':
            return False
    return True

def remove_line(board, row):
    ''' Remove the line from the board. '''
    del board[row]
    board.insert(0, ['.'] * BOARD_WIDTH)

def is_on_board(row, column):
    ''' Check, if the position is on the board. '''
    return 0 <= column < BOARD_WIDTH and row < BOARD_HEIGHT

def remove_complete_lines(board):
    ''' Remove all complete lines from the board. '''
    lines_removed = 0
    for row in range(BOARD_HEIGHT):
        if is_line_complete(board, row):
            remove_line(board, row)
            lines_removed += 1
    return lines_removed

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
    game_board = create_board()
    piece = create_piece()
    last_move = time.time()
    #clock = pg.time.Clock()
    score = 0
    while True:
        screen.fill((0, 0, 0))

        if time.time() - last_move > 0.5:
            piece['row'] += 1
            last_move = time.time()

        draw_shape(screen, piece)
        pg.draw.rect(screen, BLUE, [100, 50, 10 * 20 + 10, 20 * 20 + 10], 5)

        draw_board(screen, game_board)
        print_score(screen, score)
        check_keypress(game_board, piece)

        if not position_valid(game_board, piece, adj_row=1):
            game_board = update_board(game_board, piece)
            removed_lines = remove_complete_lines(game_board)
            score += removed_lines
            piece = create_piece()

        pg.display.update()
        for _ in pg.event.get(pg.QUIT):
            pg.quit()
            sys.exit()

        #clock.tick(10)

if __name__ == '__main__':
    game()
