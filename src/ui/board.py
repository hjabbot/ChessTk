import tkinter as tk

from constants.ui import (
    BOARD_SIZE,
    BOARD_SQUARE_SIZE,
    DARK_SQUARE_COLOUR,
    GRIDSIZE,
    HIGHLIGHT_COLOUR,
    LIGHT_SQUARE_COLOUR,
)
from coordinates import Coordinates
from gamestate import Gamestate


class Board(tk.Frame):
    # Customising a Tkinter Frame
    def __init__(self, parent):
        # Initialise like a normal Tkinter Frame
        super().__init__(parent)

        # Add a canvas to draw on
        self.canvas = tk.Canvas(
            self, 
            width=BOARD_SIZE, 
            height=BOARD_SIZE
        )
        self.canvas.pack(expand=True)

        # Bind events to actions
        self.canvas.bind("<Button-1>", self.on_click)

        # Initialise a gamestate to display
        self.gamestate = Gamestate()

        # Draw components on the board
        self.draw_board()
        self.draw_pieces()

        # Initialise special squares to potentially draw
        self.highlight_square = None


    def draw_board(self):
        """Creates a chessboard within the canvas
        """
        colors = [LIGHT_SQUARE_COLOUR, DARK_SQUARE_COLOUR]
        for row in range(GRIDSIZE):
            for col in range(GRIDSIZE):
                color = colors[(row + col) % 2]
                x1 = col * BOARD_SQUARE_SIZE
                y1 = row * BOARD_SQUARE_SIZE
                x2 =  x1 + BOARD_SQUARE_SIZE
                y2 =  y1 + BOARD_SQUARE_SIZE
                
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color
                )
    def draw_pieces(self):
        """Draws each piece on the board
        """
        for piece in self.gamestate.pieces:
            piece.initialise_img_tk()
            self.canvas.create_image(piece.coords.x, piece.coords.y, 
                                     anchor='sw', image=piece.img_tk)

    def _square_from_event(self, event):
        """Determines square that was clicked

        Args:
            event (tk.Event): LMB click event

        Returns:
            Coordinates: Coordinate object of square that was clicked on
        """
        # Get x, 8 in grid coods e.g. 0,..,7
        file = int(((BOARD_SIZE - event.y) / BOARD_SQUARE_SIZE) // 1 + 1)
        rank = int((event.x / BOARD_SQUARE_SIZE) // 1)
        # Get actual square label
        file = str(file)
        rank = chr(rank + ord('a'))
        # Turn into a coordinate object
        square = Coordinates(rank + file)

        return square

    def on_click(self, event):
        """
        Events to compute when a LMB click is registered

        Args:
            event (tk.Event): Event that triggers callback (LMB in this case)
        """
        self.canvas.delete(self.highlight_square)

        # Retrieve coordinates that were clicked
        square = self._square_from_event(event)

        # Highlight the clicked square
        self.highlight_square = self.canvas.create_rectangle(
                                    square.square_min_x,square.square_min_y,
                                    square.square_max_x,square.square_max_y,
                                    fill=HIGHLIGHT_COLOUR
        )
        # Selects piece at that square if it exists (None if it doesn't)
        selected_piece = next((p for p in self.gamestate.pieces 
                               if p.coords.bitboard == square.bitboard), 
                               None)

        # Test selection
        if selected_piece:
            print(selected_piece.id)

        self.draw_pieces()

