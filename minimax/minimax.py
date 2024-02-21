from copy import deepcopy
from checkers.constants import BLACK, WHITE


def minimax(state, depth, maximizing_player):
    """
    Implementation of the minimax algorithm with alpha-beta pruning.

    Args:
        state (Board): The current state of the game.
        depth (int): The depth to which the algorithm should search.
        maximizing_player (bool): Indicates whether it's the maximizing player's turn.

    Returns:
        tuple: A tuple containing the evaluation value and the best move found.
    """
    if depth == 0 or state.winner() is not None:
        return state.evaluate(), state

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(state, BLACK):
            evaluation = minimax(move, depth - 1, False)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(state, WHITE):
            evaluation = minimax(move, depth - 1, True)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move


def simulate_move(piece, move, board, skip):
    """
    Simulates a move on the board.

    Args:
        piece (Piece): The piece to move.
        move (tuple): The destination coordinates for the piece.
        board (Board): The current board state.
        skip (Piece): Optional. If there's a piece to skip, it should be provided.

    Returns:
        Board: The resulting board after making the move.
    """
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color):
    """
    Generates all possible moves for a given color on the board.

    Args:
        board (Board): The current board state.
        color (int): The color of the player whose moves are being generated.

    Returns:
        list: A list of all possible board states after making each move.
    """
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves
