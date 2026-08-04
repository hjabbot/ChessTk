from PIL import ImageTk

from constants.gamestate import LIGHT, DARK


class Piece:
    def __init__(self, id, img, coords):
        self.id = id
        self.side = DARK if id[0] == 'd' else LIGHT
        self.img = img
        self.coords = coords

    def initialise_img_tk(self):
        self.img_tk = ImageTk.PhotoImage(self.img)