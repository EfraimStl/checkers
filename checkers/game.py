import pygame
from .constants import WHITE, BLACK, RED, SQUARE_SIZE
from .board import Board


class Game:
    def __init__(self, window):
        """
        Initialize the Game object.

        Args:
            window: The Pygame window surface.
        """
        self.__init()
        self.window = window

    def draw(self):
        """
        Draw the game board and valid move indicators.
        """
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def __init(self):
        """
        Initialize game state variables.
        """
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def reset(self):
        """
        Reset the game state to its initial state.
        """
        self.__init()

    def select(self, row, col):
        """
        Select a piece on the board.

        Args:
            row: The row index of the selected piece.
            col: The column index of the selected piece.

        Returns:
            bool: True if a piece is successfully selected, False otherwise.
        """
        if self.selected:
            result = self.__move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False

    def __move(self, row, col):
        """
        Move the selected piece to a new position.

        Args:
            row: The row index of the target position.
            col: The column index of the target position.

        Returns:
            bool: True if the move is successful, False otherwise.
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            return True
        return False

    def draw_valid_moves(self, moves):
        """
        Draw indicators for valid moves.

        Args:
            moves (dict): A dictionary containing valid moves as keys and skipped positions as values.
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, RED,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        """
        Change the current turn to the next player.
        """
        self.valid_moves = {}
        self.turn = WHITE if self.turn == BLACK else BLACK

    def winner(self):
        """
        Determine the winner of the game.

        Returns:
            str or None: The color of the winning player (WHITE or BLACK), or None if there is no winner yet.
        """
        if self.board.all_red <= 0:
            return WHITE
        elif self.board.all_white <= 0:
            return BLACK
