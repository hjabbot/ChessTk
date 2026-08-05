import tkinter as tk

from constants.ui import (
    BOARD_PADDING,
    BOARD_SIZE,
    WINDOW_BACKGROUND_COLOR,
)
from ui.board import Board


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Chessboard")
        self.geometry(f"{BOARD_SIZE + BOARD_PADDING}x{BOARD_SIZE + BOARD_PADDING}")
        self.configure(bg=WINDOW_BACKGROUND_COLOR)

        self.board = Board(self)
        self.board.pack()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
