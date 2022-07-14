import pygame
import sys

# import time
from pygame import MOUSEBUTTONDOWN

from Piece import Pieces
import Piece as Pi

WIDTH = HEIGHT = 800
DIMENSIONS = 8
SQUARE = WIDTH // DIMENSIONS

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (195, 216, 228)  # Made these in case pure white and black interfere with the
DARK_BLUE = (78, 109, 128)  # colors of the pieces

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

board = [['  ' for i in range(8)] for j in range(8)]

pieces = {}  # Dictionary to assign piece names to their piece objects
''' To access piece images call from dictionary pieces. Ex: pieces['white_king'] '''

piece_names = ['white_king', 'white_queen', 'white_rook', 'white_bishop', 'white_knight', 'white_pawn',
               'black_king', 'black_queen', 'black_rook', 'black_bishop', 'black_knight', 'black_pawn']

for p in piece_names:
    new_piece = Pieces(p, p[0], "piece_images/" + p + ".png")
    pieces[p] = new_piece

# assigned indexes to pieces using the pieces dictionary
piece_loc = {(0, 0): pieces["white_rook"], (0, 1): pieces["white_knight"],
             (0, 2): pieces["white_bishop"], (0, 3): pieces["white_queen"], (0, 4): pieces["white_king"],
             (0, 5): pieces["white_bishop"], (0, 6): pieces["white_knight"], (0, 7): pieces["white_rook"],
             (1, 0): pieces["white_pawn"], (1, 1): pieces["white_pawn"], (1, 2): pieces["white_pawn"],
             (1, 3): pieces["white_pawn"], (1, 4): pieces["white_pawn"], (1, 5): pieces["white_pawn"],
             (1, 6): pieces["white_pawn"], (1, 7): pieces["white_pawn"],
             (2, 0): " ", (2, 1): " ", (2, 2): " ", (2, 3): " ", (2, 4): " ", (2, 5): " ", (2, 6): " ", (2, 7): " ",
             (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): " ", (3, 4): " ", (3, 5): " ", (3, 6): " ", (3, 7): " ",
             (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " ", (4, 5): " ", (4, 6): " ", (4, 7): " ",
             (5, 0): " ", (5, 1): " ", (5, 2): " ", (5, 3): " ", (5, 4): " ", (5, 5): " ", (5, 6): " ", (5, 7): " ",
             (6, 0): pieces["black_pawn"], (6, 1): pieces["black_pawn"], (6, 2): pieces["black_pawn"],
             (6, 3): pieces["black_pawn"],
             (6, 4): pieces["black_pawn"], (6, 5): pieces["black_pawn"], (6, 6): pieces["black_pawn"],
             (6, 7): pieces["black_pawn"], (7, 0): pieces["black_rook"], (7, 1): pieces["black_knight"],
             (7, 2): pieces["black_bishop"], (7, 3): pieces["black_queen"], (7, 4): pieces["black_king"],
             (7, 5): pieces["black_bishop"], (7, 6): pieces["black_knight"], (7, 7): pieces["black_rook"]}

# for testing
empty_piece_loc = \
    {(0, 0): " ", (0, 1): " ", (0, 2): " ", (0, 3): " ", (0, 4): " ", (0, 5): " ", (0, 6): " ", (0, 7): " ",
     (1, 0): " ", (1, 1): " ", (1, 2): " ", (1, 3): " ", (1, 4): " ", (1, 5): " ", (1, 6): " ", (1, 7): " ",
     (2, 0): " ", (2, 1): " ", (2, 2): " ", (2, 3): " ", (2, 4): " ", (2, 5): " ", (2, 6): " ", (2, 7): " ",
     (3, 0): " ", (3, 1): " ", (3, 2): " ", (3, 3): " ", (3, 4): " ", (3, 5): " ", (3, 6): " ", (3, 7): " ",
     (4, 0): " ", (4, 1): " ", (4, 2): " ", (4, 3): " ", (4, 4): " ", (4, 5): " ", (4, 6): " ", (4, 7): " ",
     (5, 0): " ", (5, 1): " ", (5, 2): " ", (5, 3): " ", (5, 4): " ", (5, 5): " ", (5, 6): " ", (5, 7): " ",
     (6, 0): " ", (6, 1): " ", (6, 2): " ", (6, 3): " ", (6, 4): " ", (6, 5): " ", (6, 6): " ", (6, 7): " ",
     (7, 0): " ", (7, 1): " ", (7, 2): " ", (7, 3): " ", (7, 4): " ", (7, 5): " ", (7, 6): " ", (7, 7): " "}


def empty_board(piece_dict):
    for key in piece_dict:
        piece_dict[key] = " "


# places the pieces on the board given the index
for key_coord in piece_loc:
    x_c, y_c = key_coord
    try:
        board[x_c][y_c] = piece_loc.get(key_coord).name
    except AttributeError:
        board[x_c][y_c] = piece_loc.get(key_coord)


# prints the board function
def print_board():
    for i in range(8):
        print(board[i])


# move(selected_index). Takes in selected index and runs the move algorithm in pieces for the piece
# does not give legal moves, outputs every possible move the selected pieces can make in a given position
# works for either color piece because it does not check for legality
# black and white pawns are the exception because they move unidirectional
# needs to be passed through validate_moves() to get rid of the illegal moves
def get_possible_moves(selected_index: (int, int), white_move: bool, king_index: (int, int)) -> list[(int, int)]:
    r, c = selected_index
    selected_piece = piece_loc[r, c]
    piece_name = selected_piece.name

    if piece_name == 'white_pawn':
        moves = Pi.pawn_move_white(selected_index, piece_loc)
    elif piece_name == 'black_pawn':
        moves = Pi.pawn_move_black(selected_index, piece_loc)
    elif piece_name == 'white_rook' or piece_name == 'black_rook':
        moves = Pi.rook_move(selected_index, piece_loc, white_move)
    elif piece_name == 'white_bishop' or piece_name == 'black_bishop':
        moves = Pi.bishop_move(selected_index, piece_loc, white_move)
    elif piece_name == 'white_knight' or piece_name == 'black_knight':
        moves = Pi.knight_move(selected_index, piece_loc, white_move)
    elif piece_name == 'white_queen' or piece_name == 'black_queen':
        moves = Pi.queen_move(selected_index, piece_loc, white_move)
    else:
        moves = Pi.king_move(selected_index, piece_loc, white_move)

    checked = []
    for move in moves:
        copy = piece_loc.copy()
        temp = copy[selected_index]
        copy[move] = temp
        copy[selected_index] = ' '
        if 'king' in piece_name:
            checks = Pi.check_king_attacked(copy, move, white_move)
        else:
            checks = Pi.check_king_attacked(copy, king_index, white_move)
        if not checks:
            checked.append(move)
    return checked


def check_if_mate(king_index: (int, int), is_white: bool) -> bool:
    color = 'b'
    if is_white:
        color = 'w'

    pos_moves = []
    for key in piece_loc:
        temp = piece_loc[key]
        if temp != ' ':
            if temp.color == color:
                moves = get_possible_moves(key, is_white, king_index)
                pos_moves += moves
                if pos_moves:
                    return False
    return True


'''Above is piece movement and placement 
-
-
-
-
-
-
-
-
From here down is building the project, running main, tile generation etc'''


class Tile:
    def __int__(self, index: (int, int), chess_id, color, current_piece=' '):
        self.index = index
        self.chess_id = chess_id
        self.color = color
        self.current_piece = current_piece

    def draw(self, win):
        x, y = self.index
        scale = WIDTH / DIMENSIONS
        pygame.draw.rect(win, self.color, (x * scale, y * scale, scale, scale))

    def get_center(self):
        x, y = self.index
        scale = WIDTH / DIMENSIONS
        return x * scale + (scale / 2), y * scale + (scale / 2)


# Generates all tiles and defines the colors/specifications uses the draw function in tile'''
def tile_generator(win, in_check=(-1, -1), pos_moves=None):
    if pos_moves is None:
        pos_moves = []
    font = pygame.font.Font(None, 25)
    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            chosen_tile_color = DARK_BLUE
            opposite_color = WHITE
            if (i + j) % 2 == 0:
                chosen_tile_color = WHITE
                opposite_color = BLACK

            # generates tiles given color choices above
            temp_tile = Tile()
            temp_tile.index = (i, j)
            temp_tile.chess_id = str(chr(j + 65)) + str(i + 1)

            # checks to see if tile needs to be highlighted
            if temp_tile.index in pos_moves:
                temp_tile.color = LIGHT_BLUE
                tile_color = YELLOW
            else:
                temp_tile.color = chosen_tile_color
                tile_color = opposite_color
            if temp_tile.index == in_check:
                temp_tile.color = RED

            temp_tile.draw(win)

            # generates tile chess coordinate
            # text = font.render(temp_tile.chess_id, True, opposite_color)
            if i == 0 or j == 0:
                text = font.render(temp_tile.chess_id, True, tile_color)
                text_rect = text.get_rect(
                    center=(i * SQUARE + SQUARE - (SQUARE / 7), j * SQUARE + SQUARE - (SQUARE / 10)))
                window.blit(text, text_rect)

    # draw_grid(window, WIDTH, WIDTH)  # adds a lot of lag
    place_pieces(window)
    pygame.display.update()


# Draws a grid to outline the tiles
def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


# Places pieces and their images on starting tiles.
def place_pieces(win):
    for key in piece_loc:
        x_co, y_co = key
        try:
            piece_loc[key].active_image = pygame.image.load(piece_loc[key].image)
            piece_loc[key].active_image.convert()
            win.blit(piece_loc[key].active_image, pygame.Rect(x_co * SQUARE + SQUARE / 5,
                                                              y_co * SQUARE + SQUARE / 5, SQUARE, SQUARE))
        except AttributeError:
            pass


# Takes in mouse position and outputs the rank and file of the tile to be used for identification
def get_tile(mouse_pos):
    x, y = mouse_pos
    rank = x // SQUARE
    file = y // SQUARE
    return rank, file


# takes in the move history generated in the main function and writes to a file in the project folder
# the games move history
# The game played:
# 1 d4 | d5
# 2 knf3 | bd3
# etc
def return_pgn_file(move_history: list[(int, int)]):
    raise NameError("Unimplemented")


def main():
    pygame.init()
    print_board()
    tile_generator(window)

    in_check = (-1, -1)
    pos_moves = []
    last_two_tile = []  # Tracks last two clicks of user
    move_log = []  # Tuple that stores previously executed moves
    king_index = [(0, 4), (7, 4)]
    white_move = True

    while True:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:  # Two clicks to move, not drag and drop.
                mouse_coords = pygame.mouse.get_pos()
                selected_tile = get_tile(mouse_coords)

                if check_if_mate(king_index[0], True):
                    print("Black Wins!")
                    # return False
                elif check_if_mate(king_index[1], False):
                    print("White Wins!")
                    # return False

                # if there are no tiles in last_two_tile, appends the current tile to last_two_tiles
                # also gets the possible moves, validates them, and highlights them on the board
                elif len(last_two_tile) == 0:
                    # catches an attribute error if the selected tile has no piece
                    try:
                        if white_move and piece_loc[selected_tile].color == 'w':
                            pos_moves = get_possible_moves(selected_tile, white_move, king_index[0])
                            tile_generator(window, in_check, pos_moves)
                            last_two_tile.append(selected_tile)
                        if not white_move and piece_loc[selected_tile].color == 'b':
                            pos_moves = get_possible_moves(selected_tile, white_move, king_index[1])
                            tile_generator(window, in_check, pos_moves)
                            last_two_tile.append(selected_tile)
                    except AttributeError:
                        print("No piece selected or wrong turn")

                # if the length of last_two_tiles is 1 and the selected tile is in it
                # this if statement reverts the board back
                elif selected_tile in last_two_tile and len(last_two_tile) == 1:  # Double click square is undo
                    last_two_tile.clear()  # clears last 2 tuple
                    pos_moves = []  # clears possible moves
                    tile_generator(window, in_check)  # un highlights

                # once there are two tiles in last_two_tile, the board works to move the piece
                else:
                    last_two_tile.append(selected_tile)
                    start_rank = last_two_tile[0][0]
                    start_file = last_two_tile[0][1]
                    end_rank = last_two_tile[1][0]
                    end_file = last_two_tile[1][1]
                    last_two_tile.clear()
                    chosen_piece = piece_loc.get((start_rank, start_file))

                    if (end_rank, end_file) in pos_moves:
                        pygame.Rect.move(chosen_piece.active_image.get_rect(),
                                         end_rank * SQUARE + SQUARE / 5, end_file * SQUARE + SQUARE / 5)

                        if 'king' in piece_loc[(start_rank, start_file)].name:
                            if piece_loc[(start_rank, start_file)].color == 'w':
                                king_index[0] = (end_rank, end_file)
                            else:
                                king_index[1] = (end_rank, end_file)

                        piece_loc[(end_rank, end_file)] = piece_loc[start_rank, start_file]
                        piece_loc[start_rank, start_file] = ' '
                        board[end_rank][end_file] = board[start_rank][start_file]
                        board[start_rank][start_file] = ' '

                        if Pi.check_king_attacked(piece_loc, king_index[0], True):
                            in_check = king_index[0]
                        elif Pi.check_king_attacked(piece_loc, king_index[1], False):
                            in_check = king_index[1]
                        else:
                            in_check = (-1, -1)

                        tile_generator(window, in_check)

                        move_log.append([(start_rank, start_file), (end_rank, end_file)])

                        pygame.display.update()
                        if piece_loc[(end_rank, end_file)].color == 'w':
                            white_move = False
                        if piece_loc[(end_rank, end_file)].color == 'b':
                            white_move = True
                    else:
                        tile_generator(window, in_check)  # un highlights if selected no tile
                        print("impossible move")

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:  # Z for undo (Like ctrl + z)
                    if len(move_log) != 0:  # No moves have been made
                        # update_it_all(end_rank, end_file, start_rank, start_file)
                        pass
                        # ^^ This function makes life easy, thanks for that. Only issue is captured piece not being
                        # returned to original square.
                    else:
                        pass
                else:
                    pass
            else:
                pass


if __name__ == "__main__":
    main()
