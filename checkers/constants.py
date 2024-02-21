import pygame.image

WIDTH = HEIGHT = 600
ROWS = COLS = 8
SQUARE_SIZE = WIDTH // COLS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_SQUARE_COLOR = (95, 122, 97)
DARK_SQUARE_COLOR = (84, 93, 73)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

try:
    CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (40, 20))
except pygame.error as e:
    print("Error loading crown image:", e)
    CROWN = pygame.Surface((40, 20))  # Placeholder image
    CROWN.fill(GRAY)  # Placeholder color

"""
Module Constants:
    This module contains constants used in the checkers game.
    - WIDTH: Width of the game window.
    - HEIGHT: Height of the game window.
    - ROWS: Number of rows on the game board.
    - COLS: Number of columns on the game board.
    - SQUARE_SIZE: Size of each square on the game board.
    - BLACK: RGB color code for black.
    - WHITE: RGB color code for white.
    - LIGHT_SQUARE_COLOR: RGB color code for light squares on the game board.
    - DARK_SQUARE_COLOR: RGB color code for dark squares on the game board.
    - RED: RGB color code for red.
    - GRAY: RGB color code for gray.
    - CROWN: Image of the crown used for kings in the game.
"""
