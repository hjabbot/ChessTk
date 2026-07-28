import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self, board_size=480, padding=40):
        super().__init__()
        self.title("Tkinter Chessboard")
        self.geometry(f"{board_size + padding}x{board_size + padding}") # Extra space for frame padding
        self.configure(bg="#2b2b2b")        # Dark window background
        
        # 1. Create a frame wrapper with a border and padding
        self.board_frame = tk.Frame(self, bg="#1a1a1a")
        self.board_frame.pack()
        
        # 2. Place the canvas inside the frame
        self.canvas = tk.Canvas(
            self.board_frame, 
            width=board_size, 
            height=board_size
        )
        self.canvas.pack()

        # 3. Draw the board in the canvas
        self.square_size = board_size // 8
        self.draw_board()

    def draw_board(self):
        colors = ["#B58863", "#F0D9B5"] # Standard chess color palette
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, outline=""
                )

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
