import tkinter as tk

from constants.ui import (
    BOARD_D_COLOR,
    BOARD_L_COLOR,
    BOARD_PADDING,
    BOARD_SIZE,
    BOARD_SQUARE_SIZE,
    GRIDSIZE,
    WINDOW_BACKGROUND_COLOR,
)
from gamestate import Gamestate


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Chessboard")
        self.geometry(f"{BOARD_SIZE + BOARD_PADDING}x{BOARD_SIZE + BOARD_PADDING}")
        self.configure(bg=WINDOW_BACKGROUND_COLOR)
        
        self.create_board()
        self.draw_board()
        self.gamestate = Gamestate()
        self.draw_pieces()

    def create_board(self):
        # Create a frame wrapper with a border and padding
        self.board_frame = tk.Frame(self, bg=WINDOW_BACKGROUND_COLOR)
        self.board_frame.pack(fill=tk.BOTH, expand=True)
        
        # Place the canvas inside the frame
        self.board_canvas = tk.Canvas(
            self.board_frame, 
            width=BOARD_SIZE, 
            height=BOARD_SIZE
        )
        self.board_canvas.pack(expand=True)

        return True

    def draw_board(self):
        colors = [BOARD_L_COLOR, BOARD_D_COLOR]
        for row in range(GRIDSIZE):
            for col in range(GRIDSIZE):
                color = colors[(row + col) % 2]
                x1 = col * BOARD_SQUARE_SIZE
                y1 = row * BOARD_SQUARE_SIZE
                x2 =  x1 + BOARD_SQUARE_SIZE
                y2 =  y1 + BOARD_SQUARE_SIZE
                
                self.board_canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color
                )

    def draw_pieces(self):
        for piece in self.gamestate.pieces:
            piece.initialise_img_tk()
            self.board_canvas.create_image(piece.coords.x, piece.coords.y, 
                                     anchor='sw', image=piece.img_tk)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
