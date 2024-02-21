import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK
from checkers.game import Game
from minimax.minimax import minimax

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

FPS = 60


def get_pos_from_mouse(pos):
    """
    Convert mouse position to board position.

    Args:
        pos (tuple): The mouse position as a tuple (x, y).

    Returns:
        tuple: The board position as a tuple (row, col).
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    """
    Main function to run the game loop.
    """
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == BLACK:
            value, new_board = minimax(game.get_board(), 4, BLACK)
            game.minimax_move(new_board)

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                game.select(row, col)

        game.draw()

    pygame.quit()


main()
