import pygame
from .constants import DARK_SQUARE_COLOR, ROWS, BLACK, SQUARE_SIZE, COLS, WHITE, LIGHT_SQUARE_COLOR
from .piece import Piece


class Board:
    def __init__(self):
        """
        Initialize the Board object.
        """
        self.board = []
        self.all_black = self.all_white = 12
        self.black_kings = self.white_kings = 0
        self.create_board()

    def move(self, piece, row, col):
        """
        Move a piece on the board to a new position.

        Args:
            piece (Piece): The piece to be moved.
            row (int): The row index of the target position.
            col (int): The column index of the target position.
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == 7 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1

    def get_piece(self, row, col):
        """
        Get the piece at the specified position on the board.

        Args:
            row (int): The row index of the position.
            col (int): The column index of the position.

        Returns:
            Piece or int: The piece object at the specified position, or 0 if the position is empty.
        """
        return self.board[row][col]

    def draw_squares(self, window):
        """
        Draw the squares of the board.

        Args:
            window: The Pygame window surface.
        """
        window.fill(DARK_SQUARE_COLOR)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, LIGHT_SQUARE_COLOR, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        """
        Create the initial state of the board.
        """
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 != row % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, window):
        """
        Draw the entire board.

        Args:
            window: The Pygame window surface.
        """
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    def winner(self):
        """
        Determine the winner of the game.

        Returns:
            str or None: The color of the winning player (WHITE or BLACK), or None if there is no winner yet.
        """
        if self.all_black <= 0:
            return WHITE
        elif self.all_white <= 0:
            return BLACK

    def remove(self, pieces):
        """
        Remove pieces from the board.

        Args:
            pieces (list): A list of pieces to be removed.
        """
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.all_black -= 1
                else:
                    self.all_white -= 1

    def get_valid_moves(self, piece):
        """
        Get the valid moves for a given piece.

        Args:
            piece (Piece): The piece for which to find valid moves.

        Returns:
            dict: A dictionary containing valid moves as keys and skipped positions as values.
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == WHITE or piece.king:
            moves.update(self.__traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self.__traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == BLACK or piece.king:
            moves.update(self.__traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self.__traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def __traverse_left(self, start, stop, step, color, left, skipped=[]):
        """
        Recursively traverse to the left of a piece to find valid moves.
        """
        moves = {}
        last = []
        for i in range(start, stop, step):

            if left < 0:
                break

            current = self.board[i][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i, left)] = last + skipped
                else:
                    moves[(i, left)] = last

                if last:
                    if step == -1:
                        row = max(i - 3, 0)
                    else:
                        row = min(i + 3, ROWS)
                    moves.update(self.__traverse_left(i + step, row, step, color, left - 1, skipped=last))
                    moves.update(self.__traverse_right(i + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def __traverse_right(self, start, stop, step, color, right, skipped=[]):
        """
        Recursively traverse to the right of a piece to find valid moves.
        """
        moves = {}
        last = []
        for i in range(start, stop, step):

            if right >= COLS:
                break

            current = self.board[i][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i, right)] = last + skipped
                else:
                    moves[(i, right)] = last

                if last:
                    if step == -1:
                        row = max(i - 3, 0)
                    else:
                        row = min(i + 3, ROWS)
                    moves.update(self.__traverse_left(i + step, row, step, color, right - 1, skipped=last))
                    moves.update(self.__traverse_right(i + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def evaluate(self):
        """
        Evaluate the current board state.

        Returns:
            int: The evaluation value of the board state.
        """
        return self.all_black - self.all_white + (self.black_kings * 0.5 - self.white_kings * 0.5)

    def get_all_pieces(self, color):
        """
        Get all pieces of a given color on the board.

        Args:
            color (int): The color of the pieces to retrieve.

        Returns:
            list: A list of pieces of the specified color.
        """
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
