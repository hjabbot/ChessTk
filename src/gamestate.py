import cython  # noqa: I001

from constants.gamestate import DARK, LIGHT, INITIAL_BOARD
from constants.ui import (
    SPRITE_D_BISHOP,
    SPRITE_D_KING,
    SPRITE_D_KNIGHT,
    SPRITE_D_PAWN,
    SPRITE_D_QUEEN,
    SPRITE_D_ROOK,
    SPRITE_L_BISHOP,
    SPRITE_L_KING,
    SPRITE_L_KNIGHT,
    SPRITE_L_PAWN,
    SPRITE_L_QUEEN,
    SPRITE_L_ROOK,
)
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
                id = piece_positions[y][x]
                
                if   id == '..':    continue
                elif id == 'dp':    img = SPRITE_D_PAWN
                elif id == 'lp':    img = SPRITE_L_PAWN
                elif id == 'dR':    img = SPRITE_D_ROOK
                elif id == 'lR':    img = SPRITE_L_ROOK
                elif id == 'dN':    img = SPRITE_D_KNIGHT
                elif id == 'lN':    img = SPRITE_L_KNIGHT
                elif id == 'dB':    img = SPRITE_D_BISHOP
                elif id == 'lB':    img = SPRITE_L_BISHOP
                elif id == 'dQ':    img = SPRITE_D_QUEEN
                elif id == 'lQ':    img = SPRITE_L_QUEEN
                elif id == 'dK':    img = SPRITE_D_KING
                elif id == 'lK':    img = SPRITE_L_KING

                pieces += [Piece(id, img, Coordinates(file+rank))]
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
        