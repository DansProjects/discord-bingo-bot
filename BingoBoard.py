from PIL import Image,ImageDraw,ImageFont
import textwrap
from random import randint
class BingoBoard:

    def __init__(self, bingo_board):
        self.bingo_board = bingo_board

    def generate_board_image(self, file_name = 'bingo'):

        #set font to comic sans for maximum meme
        font = ImageFont.truetype("fonts/comic-sans.ttf", 28, encoding="unic")

        #boxes are 250px by 250px with 10px margins
        #approx 15 characers per line
        canvas = Image.open("bingo_template.png")
        draw = ImageDraw.Draw(canvas)
        
        initialXPosition = 100
        initialYPosition = 450
        
        x = initialXPosition
        y = initialYPosition
        
        cellWidth = 265
        cellHeight = 260
        margin = 10

        for row in self.bingo_board:

            for cell in row:
                #make sure no line goes past 13 characters
                text = textwrap.fill(cell[0], 13)
                draw.text((x, y), text, 'blue', font)
                x = x + cellWidth

            x = initialXPosition
            y = y + cellHeight

        file_dir = 'bingo_boards/'

        rand_file_int = randint(0, 1333337);
        file_name = file_dir+file_name+'_'+str(rand_file_int)+'.png'

        # save the blank canvas to a file
        canvas.save(file_name, "PNG")

        return file_name
