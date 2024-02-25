''' This module contains the GameBoard class. '''

class GameBoard:
    ''' A class to represent the game board. '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [['.' for _ in range(self.width)] for _ in range(self.height)]
