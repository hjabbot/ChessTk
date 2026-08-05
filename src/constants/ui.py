# .......................................................................... Size
GRIDSIZE = 8
BOARD_SIZE = 640
BOARD_PADDING = 40
BOARD_SQUARE_SIZE = BOARD_SIZE / GRIDSIZE


# .......................................................................... Window
WINDOW_BACKGROUND_COLOR = "#2b2b2b"


# .......................................................................... Sprite
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




# .......................................................................... Colour
SCOREBAR_BORDER_COLOUR	= 'black'

SIDEBAR_BACKGROUND_COLOUR = 'wheat'

DARK_SQUARE_COLOUR	= 'darkolivegreen4'
LIGHT_SQUARE_COLOUR	= 'beige'

SELECTION_COLOUR 			= 'deepskyblue'
SELECTION_BORDER_THICKNESS 	= BOARD_SQUARE_SIZE // 10
SELECTION_ALPHA  			= 150

HIGHLIGHT_COLOUR 	= 'gold'
HIGHLIGHT_ALPHA  	= 150

CHECK_COLOUR		= 'firebrick'

MOVES_COLOUR 		= 'deepskyblue'
MOVES_ALPHA 		= 150