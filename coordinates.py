from constants import BOARD_SQUARE_SIZE, BOARD_SIZE

class Coordinates:
    def __init__(self,coords):
        self.file  = coords[0]
        self.rank = coords[1]

    @property
    def x(self):
        position = ord(self.rank) - ord('1')
        return position * BOARD_SQUARE_SIZE

    @property
    def y(self):
        position = ord(self.file) - ord('a')
        return BOARD_SIZE - position * BOARD_SQUARE_SIZE