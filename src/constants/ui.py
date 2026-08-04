### Board Constants
GRIDSIZE = 8
BOARD_SIZE = 640
BOARD_PADDING = 40
BOARD_SQUARE_SIZE = BOARD_SIZE / GRIDSIZE
BOARD_D_COLOR = "#B58863"
BOARD_L_COLOR = "#F0D9B5"


### Window Constants
WINDOW_BACKGROUND_COLOR = "#2b2b2b"


### Sprites

# 1. Convert to format that Tkinter can use (png)
from cairosvg import svg2png
from PIL import Image
from io import BytesIO

def _create_image(filename, width=BOARD_SQUARE_SIZE, height=BOARD_SQUARE_SIZE):
    '''
    Creates a png from svg input without writing to file
    '''
    png_data = svg2png(url=filename,
                       output_width=width,
                       output_height=height)
    image = Image.open(BytesIO(png_data))
    return image

# 2. Define each sprite
SPRITE_L_PAWN   = _create_image("assets/sprites/l_pawn.svg")
SPRITE_D_PAWN   = _create_image("assets/sprites/d_pawn.svg")
SPRITE_L_ROOK   = _create_image("assets/sprites/l_rook.svg")
SPRITE_D_ROOK   = _create_image("assets/sprites/d_rook.svg")
SPRITE_L_KNIGHT = _create_image("assets/sprites/l_knight.svg")
SPRITE_D_KNIGHT = _create_image("assets/sprites/d_knight.svg")
SPRITE_L_BISHOP = _create_image("assets/sprites/l_bishop.svg")
SPRITE_D_BISHOP = _create_image("assets/sprites/d_bishop.svg")
SPRITE_L_QUEEN  = _create_image("assets/sprites/l_queen.svg")
SPRITE_D_QUEEN  = _create_image("assets/sprites/d_queen.svg")
SPRITE_L_KING   = _create_image("assets/sprites/l_king.svg")
SPRITE_D_KING   = _create_image("assets/sprites/d_king.svg")