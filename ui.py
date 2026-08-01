import tkinter as tk

from constants import *
from piece import Piece
from coordinates import Coordinates

class MainWindow(tk.Tk):
    def __init__(self, board_size=BOARD_SIZE, padding=BOARD_PADDING):
        super().__init__()
        self.title("Tkinter Chessboard")
        self.geometry(f"{board_size + padding}x{board_size + padding}")
        self.configure(bg=WINDOW_BACKGROUND_COLOR)
        
        # 1. Create a frame wrapper with a border and padding
        self.board_frame = tk.Frame(self, bg=WINDOW_BACKGROUND_COLOR)
        self.board_frame.pack()
        
        # 2. Place the canvas inside the frame
        self.canvas = tk.Canvas(
            self.board_frame, 
            width=board_size, 
            height=board_size
        )
        self.canvas.pack()

        # 3. Draw the board in the canvas
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        colors = [BOARD_L_COLOR, BOARD_D_COLOR]
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
        self.light_pieces = [Piece('l_p',SPRITE_L_PAWN,Coordinates('b1'))]
        self.dark_pieces  = [Piece('d_p',SPRITE_D_PAWN,Coordinates('g1'))]

        for piece in self.light_pieces + self.dark_pieces:
            piece.initialise_img_tk()
            self.canvas.create_image(piece.coords.x, piece.coords.y, 
                                     anchor='sw', image=piece.img_tk)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
