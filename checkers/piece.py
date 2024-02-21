import pygame
from .constants import BLACK, SQUARE_SIZE, GRAY, CROWN


class Piece:
    """
    Class representing a piece in the checkers game.
    """
    PADDING = 10
    OUTLINE = 3

    def __init__(self, row, col, color):
        """
        Initialize a Piece object.

        Args:
            row (int): The row index of the piece on the board.
            col (int): The column index of the piece on the board.
            color: The color of the piece.
        """
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.pos()

    def pos(self):
        """
        Calculate the position of the piece on the board.
        """
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """
        Make the piece a king.
        """
        self.king = True

    def draw(self, window):
        """
        Draw the piece on the board.

        Args:
            window: The Pygame window surface.
        """
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            window.blit(CROWN, (self.x - CROWN.get_width()// 2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        """
        Move the piece to a new position on the board.

        Args:
            row (int): The row index of the new position.
            col (int): The column index of the new position.
        """
        self.row = row
        self.col = col
        self.pos()

    def __repr__(self):
        """
        Return a string representation of the piece.

        Returns:
            str: The color of the piece.
        """
        return str(self.color)
