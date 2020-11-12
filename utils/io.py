"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 11/11/2020 8:11 pm
File: utils.py
"""

import os
import time

import chess

import board.chess_board as b


def initialise_file(board: b.ChessBoard, file_name: str = 'game_results.txt'):
    """Initialises a new file to keep track of the current game's results.

    It will be saved inside a folder called "results", created inside the root project folder (if it doesn't exist).

    :param board: Initial state of the chess board
    :param file_name: Name of the file to be saved
    """
    if not os.path.exists('results'):
        os.makedirs('results')

    with open(file=f'results/{file_name}', mode='w', encoding='utf-8') as f:
        f.writelines(
            ['This file keeps track of the state of the board on the latest turn played.\n',
             'Lowercase letters represent black pieces and uppercase ones represent white pieces.\n\n',
             'Each piece is represented as:\n',
             '- R or r: Rook\n',
             '- N or n: Knight\n',
             '- B or b: Bishop\n',
             '- Q or q: Queen\n',
             '- K or k: King\n',
             '- P or p: Pawn\n\n',
             'The entire board is represented in a single line, from top (black side) to bottom (white side)\n',
             'Rows are separated by forward slashes (/) and empty squares are represented by dots (.)\n\n',
             f'Game: {board.white.name} (White) vs {board.black.name} (Black) - '
             f'Played at {time.strftime("%d/%m/%Y %H:%M:%S")}\n\n'
             'Current state of the board:\n\n',
             board.print_in_one_line(),
             '\n\n'])


def add_turn_to_file(board: b.ChessBoard, file_name: str = 'game_results.txt'):
    """Adds a new turn to a file that has already been initialised.

    The `seek()` function is used to update two characters in the board.

    :param board: Current state of the board
    :param file_name: Name of the file to be saved
    :raises IOError: If the file has not been initialised
    """
    if not os.path.exists(f'results/{file_name}'):
        raise IOError('The file specified does not exist')

    current_move = board.board.peek()
    from_square = chess.square_name(current_move.from_square)
    to_square = chess.square_name(current_move.to_square)

    current_piece_from = board.get_piece_at(square=from_square)
    current_piece_to = board.get_piece_at(square=to_square)

    with open(file=f'results/{file_name}', mode='r+', encoding='utf-8') as f:
        current_line = f.readline()

        while 'Current state of the board:' not in current_line:
            current_line = f.readline()

        # jump two 2 newline characters
        # we have reached the line containing the board
        initial_cursor = f.seek(f.tell() + 2)

        # get "from" position that needs to be updated
        squares_one_line = board.squares_one_line
        from_pos = squares_one_line.index(from_square)

        # seek "from" position
        f.seek(initial_cursor + from_pos)

        # replace "from" square
        if current_piece_from:
            f.write(str(current_piece_from))
        else:
            f.write('.')

        # get "to" position
        to_pos = squares_one_line.index(to_square)

        # seek "to" position
        f.seek(initial_cursor + to_pos)

        # replace "to" square
        if current_piece_to:
            f.write(str(current_piece_to))
        else:
            f.write('.')
