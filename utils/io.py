"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 11/11/2020 8:11 pm
File: utils.py
"""

import os
import board.chess_board as b
import time
import player.player as player


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
            ['This file keeps track of the state of the board and the moves on each turn from the last game played.\n',
             'Lowercase letters represent black pieces and uppercase ones represent white pieces.\n\n',
             'Each piece is represented as:\n',
             '- R or r: Rook\n',
             '- N or n: Knight\n',
             '- B or b: Bishop\n',
             '- Q or q: Queen\n',
             '- K or k: King\n',
             '- P or p: Pawn\n\n',
             f'Game: {board.white.name} (White) vs {board.black.name} (Black) - '
             f'Played at {time.strftime("%d/%m/%Y %H:%M:%S")}\n\n'
             'Initial state of the board:\n\n',
             str(board.board),
             '\n\n'])


def add_turn_to_file(board: b.ChessBoard, current_player: player.Player, file_name: str = 'game_results.txt'):
    """Adds a new turn to a file that has already been initialised.

    :param board: Current state of the board
    :param current_player: Current player
    :param file_name: Name of the file to be saved
    :raises IOError: If the file does not exist
    """
    if not os.path.exists(f'results/{file_name}'):
        raise IOError('The file specified does not exist')

    with open(file=f'results/{file_name}', mode='a', encoding='utf-8') as f:
        f.writelines([
            f'Turn {len(board.board.move_stack)} - {current_player.print_name_and_colour()}: {str(board.board.peek())}\n\n',
            str(board.board),
            '\n\n'
        ])
