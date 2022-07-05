import pygame
import time
import sys

from Piece import Pieces
import Board

board = [['  ' for i in range(8)] for i in range(8)]

'''piece declarations'''
#name, color, image, is_king = False
white_bishop = Pieces()
white_bishop.name = "bi"
white_bishop.color = "w"
white_bishop.image = "piece_images/white_bishop.png"

white_rook = Pieces()
white_rook.name = "rk"
white_rook.color = "w"
white_rook.image = "piece_images/white_rook.png"

white_knight = Pieces()
white_knight.name = "kn"
white_knight.color = "w"
white_knight.image = "piece_images/white_knight.png"

white_queen = Pieces()
white_queen.name = "qu"
white_queen.color = "w"
white_queen.image = "piece_images/white_queen.png"

white_king = Pieces()
white_king.name = "ki"
white_king.color = "w"
white_king.image = "piece_images/white_king.png"

white_pawn = Pieces()
white_pawn.name = "pa"
white_pawn.color = "w"
white_pawn.image = "piece_images/white_pawn.png"

black_bishop = Pieces()
black_bishop.name = "bi"
black_bishop.color = "b"
black_bishop.image = "piece_images/black_bishop.png"

black_rook = Pieces()
black_rook.name = "rk"
black_rook.color = "b"
black_rook.image = "piece_images/black_rook.png"

black_knight = Pieces()
black_knight.name = "kn"
black_knight.color = "b"
black_knight.image = "piece_images/black_knight.png"

black_queen = Pieces()
black_queen.name = "qu"
black_queen.color = "b"
black_queen.image = "piece_images/black_queen.png"

black_king = Pieces()
black_king.name = "ki"
black_king.color = "b"
black_king.image = "piece_images/black_king.png"

black_pawn = Pieces()
black_pawn.name = "pa"
black_pawn.color = "b"
black_pawn.image = "piece_images/black_pawn.png"

'''adds all the pieces to the appropriate squares'''


def board_setup():
    raise NameError("Unimplemented")


'''prints the board function'''


def print_board():
    raise NameError("Unimplemented")


'''move(selected_index). Takes in selected index and runs the move algorithm in pieces for the piece'''


def move(selected_index):
    raise NameError("Unimplemented")


'''I added some basic code that creates a grid on a blank canvas, from here we need to create a TILE class
that should have all the entities that go along with tiles like the chess location (a1, a2) the index (0,0)(1,1)
current piece, color, etc'''

class Tile:
    def __int__(self, index: (int, int), chess_id, color, current_piece=' '):
        self.index = index
        self.chess_id = chess_id
        self.color = color
        self.current_piece = current_piece

    def draw(self, window):
        x, y = self.index
        scale = WIDTH/8
        pygame.draw.rect(window, self.color, (x * scale, y * scale, scale, scale))



'''Generates all tiles and defines the colors/specifications uses the draw function in tile'''
def tile_generator(win, num_row):
    all_tiles = []
    tile_count = 0
    last_color_white = True
    for i in range(num_row):
        last_color_white = not last_color_white
        for j in range(num_row):
            temp_color = BLACK
            if not last_color_white:
                temp_color = WHITE
            last_color_white = not last_color_white
            temp_tile = Tile()
            temp_tile.index = (i, j)
            temp_tile.chess_id = str(chr(j + 65)) + str(i + 1)
            temp_tile.color = temp_color
            all_tiles.append(temp_tile)
            temp_tile.draw(win)

            text = font.render(temp_tile.chess_id, True, YELLOW)
            text_rect = text.get_rect(center=(i * (WIDTH / 8) + (WIDTH / 8) - 15, j * (WIDTH / 8) + (WIDTH / 8) - 10))
            window.blit(text, text_rect)

    return all_tiles


WIDTH = 800

window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Chess")

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)


def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, WHITE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, WHITE, (j * gap, 0), (j * gap, width))

'''
does not work yet, placing pieces might have to do with a dictionary and the board and has to be done 
individually 
def place_pieces(win, all_tiles):
    for i in range(4):
        for j in range(8):
            all_tiles
            img = pygame.image.load('bird.png')
            img.convert()
'''
pygame.init()
font = pygame.font.Font(None, 25)
#draw_grid(window, 8, WIDTH)
all_tiles = tile_generator(window, 8)
pygame.display.update()


while True:
    pygame.time.delay(50)

    # causes exit not to break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



