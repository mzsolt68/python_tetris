''' A module to represent a falling piece in the game. '''

import random
from shapes import SHAPES

class Piece:
    ''' A class to represent a falling piece in the game. '''
    def __init__(self):
        self.rotation = 0
        choice = random.choice(list(SHAPES.keys()))
        self.shape = SHAPES[choice]['shape']
        self.color = SHAPES[choice]['color']
        self.row = 0
        self.column = 2
        self.drop_speed = 0.5

    def move_down(self):
        ''' Move the piece down. '''
        self.row += 1

    def rotate(self):
        ''' Rotate the piece. '''
        self.rotation = (self.rotation + 1) % len(self.shape)

    def rotate_back(self):
        ''' Rotate the piece backward. '''
        self.rotation = (self.rotation - 1) % len(self.shape)

    def move_left(self):
        ''' Move the piece left. '''
        self.column -= 1

    def move_right(self):
        ''' Move the piece right. '''
        self.column += 1
