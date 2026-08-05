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
    def __init__(self, parent):
        super().__init__(parent)
        
        # Place the canvas inside the frame
        self.canvas = tk.Canvas(
            self, 
            width=BOARD_SIZE, 
            height=BOARD_SIZE
        )
        self.canvas.pack(expand=True)

        # Bind events to actions
        self.canvas.bind("<Button-1>", self.on_click)

        self.gamestate = Gamestate()

        self.draw_board()
        self.draw_pieces()
        self.highlight_square = None


    def draw_board(self):
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
        for piece in self.gamestate.pieces:
            piece.initialise_img_tk()
            self.canvas.create_image(piece.coords.x, piece.coords.y, 
                                     anchor='sw', image=piece.img_tk)

    def on_click(self, event):
        self.canvas.delete(self.highlight_square)
        # Get x, 8 in grid coods e.g. 0,..,7
        file = int((event.x / BOARD_SQUARE_SIZE) // 1 + 1)
        rank = int(((BOARD_SIZE - event.y) / BOARD_SQUARE_SIZE) // 1)
        # Get actual square label
        file = str(file)
        rank = chr(rank + ord('a'))
        square = Coordinates(rank + file)
        print(square)
        self.highlight_square = self.canvas.create_rectangle(
                                    square.square_min_x,square.square_min_y,
                                    square.square_max_x,square.square_max_y,
                                    fill=HIGHLIGHT_COLOUR
        )

        self.draw_pieces()

