from bitboard import Bitboard
from constants.ui import BOARD_SIZE, BOARD_SQUARE_SIZE, GRIDSIZE


class Coordinates:
    def __init__(self,coords):
        """
        Creates a Coordinate object that flexibly describes a position on the board

        Args:
            coords (str): Standard chess square name e.g. 'a1', 'h8'
        """
        # String coordinates
        self.coords = coords
        self.file = coords[0]
        self.rank = coords[1]

        # Numeric coordinates
        self.row = ord(self.rank) - ord('1')
        self.col = ord(self.file) - ord('a')

        # Pixel coordinates
        self.x = self.col * BOARD_SQUARE_SIZE
        self.y = BOARD_SIZE - self.row * BOARD_SQUARE_SIZE

        # Bitboard Coordinates, 
        # e.g. a1 = 000...001
        #      h8 = 100...000
        self.bitboard = Bitboard(1 << self.row * GRIDSIZE + self.col)

    def __str__(self):
        # String coordinates
        return self.coords

    @property
    def pretty_str(self):
        print(self.bitboard)