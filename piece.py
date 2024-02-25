''' A module to represent a falling piece in the game. '''

import random
from shapes import SHAPES

class Piece:
    ''' A class to represent a falling piece in the game. '''
    def __init__(self):
        self.rotation = 0
        self.shape = SHAPES[random.choice(list(SHAPES.keys()))]
        self.row = 0
        self.column = 2
