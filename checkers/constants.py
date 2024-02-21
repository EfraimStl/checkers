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

