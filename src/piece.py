from PIL import ImageTk

from constants.gamestate import DARK, LIGHT
from constants.ui import SPRITE_FROM_ID

class Piece:
    def __init__(self, id, coords):
        self.id = id
        self.side = DARK if id[0] == 'd' else LIGHT
        self.coords = coords

    def initialise_img(self, canvas):

        img = SPRITE_FROM_ID[self.id]

        self.img_png    = img
        self.img_tk     = ImageTk.PhotoImage(img)
        self.img_canvas = canvas.create_image(self.coords.x, self.coords.y, 
                                                anchor='sw', image=self.img_tk)


    def moves_available(self, enemy_piece_positions, ally_piece_positions, pin_positions):
        pass