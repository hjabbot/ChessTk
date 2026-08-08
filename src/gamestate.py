import cython  # noqa: I001

from constants.gamestate import DARK, LIGHT, INITIAL_BOARD
from piece import Piece
from coordinates import Coordinates

@cython.cclass
class Gamestate:

    def __init__(self, turn=LIGHT):
        self.pieces = self._gen_initial_pieces()
        self.light_pieces = [piece for piece in self.pieces 
                             if piece.side == LIGHT]
        self.dark_pieces  = [piece for piece in self.pieces 
                             if piece.side == DARK]

        self.turn = turn
        self.is_check = self._is_check()
        self.is_checkmate = self._is_checkmate()
        self.pins = self._pins()
        self.castling_available = self._castling_available()
        self.enpassant_available = self._enpassant_available()
        self.moves_available = self._moves_available()

    @cython.cfunc
    def _gen_initial_pieces(self, piece_positions = INITIAL_BOARD):
        """
        Initialises Piece objects based on initial board state defined in constants/gamestate.py

        Args:
            piece_positions (2D Array, optional): 
                List of piece ID's organised in 8x8 array to read in as a chess board. 
                Defaults to INITIAL_BOARD.

        Returns:
            list: List of Piece objects.
        """
        pieces = []
        for file in 'abcdefgh':
            for rank in '87654321':
                x = ord(file) - ord('a')
                y = 8 - int(rank)
                piece_id = piece_positions[y][x]
                if piece_id != '..':
                    pieces += [Piece(piece_id, Coordinates(file+rank))]
        return pieces

    @cython.cfunc
    def _is_check(self):
        pass

    @cython.cfunc
    def _is_checkmate(self):
        pass

    @cython.cfunc
    def _pins(self):
        pass

    @cython.cfunc
    def _castling_available(self):
        pass

    @cython.cfunc
    def _enpassant_available(self):
        pass

    @cython.cfunc
    def _moves_available(self):
        pass

    def make_move(self, piece, position):

        # Check if move possible
        try:
            # Ensure piece can move to position and position is available
            assert(piece.moves_available.bitboard & position.bitboard & self.moves_available)
            # Ensures piece is not pinned
            assert(piece.position.bitboard & self.pins == 0)
        except AssertionError:
            print("Move not possible")
            return False
        
        self.turn = LIGHT if self.turn == DARK else DARK
        