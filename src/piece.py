from PIL import ImageTk


class Piece:
    def __init__(self, id, img, coords):
        self.id = id
        self.img = img
        self.coords = coords

    
    def initialise_img_tk(self):
        self.img_tk = ImageTk.PhotoImage(self.img)