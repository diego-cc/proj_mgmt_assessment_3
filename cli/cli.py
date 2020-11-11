"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 11/11/2020 5:17 pm
File: cli.py
"""
import os
import time
from typing import Tuple
import colorama
import random
import chess
import sys
import player.player as player
import board.chess_board as board
import utils.io


def get_player_name(player_num: int, player_colour: int = colorama.Fore.WHITE) -> str:
    """Asks for the current player's name.

    :param player_num: Current player number (e.g. 1 or 2)
    :param player_colour: Optional foreground colour to highlight the text input
    :return: Player name
    """
    p = input(f'{player_colour}(Player {str(player_num)}) Enter your name: ')

    while not p.strip():
        print(colorama.Style.RESET_ALL)
        print('Invalid name, please try again.')
        p = input(f'{player_colour}(Player {str(player_num)}) Enter your name: ')

    print(colorama.Style.RESET_ALL)
    print()
    return p


def play_turn(p: player.Player, b: board.ChessBoard, file_name: str) -> Tuple[str, board.ChessBoard]:
    """Lets the current player `p` decide their turn.

    :param file_name: Name of an existing file to add the turn
    :param p: Current player
    :param b: Current state of the chess board
    :return: A tuple containing the move input decided by `p` and the next state of `b`, respectively
    """
    if len(b.board.move_stack):
        print(f'\nLast move: {str(b.board.peek())}')

    print(f'\nIt is now {str(p)}\'s turn.\n')
    move = input('Enter your move: ')
    print()

    if move != 'q':
        while not b.move_piece(uci_move=move):
            print('Illegal move, please try again.')
            move = input('Enter your move: ')
            print()
            if move == 'q':
                break

        utils.io.add_turn_to_file(board=b, current_player=p, file_name=file_name)

    return move, b


def start():
    """Entry point of the game."""

    print('\nWelcome! This is a basic chess game.')
    print('Your move should use standard algebraic notation, e.g. e2e4, g1f3, etc.')
    print('You do not need to add an "x" when performing captures, the program understands your intention.')
    print('Be explicit when performing castling, use a literal notation (e.g. e1h1), instead of O-O or O-O-O.')
    print('Moves that would put your own king in check are not allowed.')
    print('\nType "q" and press Enter anytime to quit the game.\n')

    p1_name = get_player_name(1)

    if p1_name.strip().lower() == 'q':
        print('\nBye!\n')
        return

    p2_name = get_player_name(2)

    if p2_name.strip().lower() == 'q':
        print('\nBye!\n')
        sys.exit(0)

    # Toss coin
    p1_colour = random.randint(0, 1)

    if p1_colour == 1:
        player_1 = player.Player(name=p1_name, colour=chess.WHITE, cli_fore=colorama.Fore.GREEN,
                                 cli_back=colorama.Back.WHITE)
        player_2 = player.Player(name=p2_name, colour=chess.BLACK, cli_fore=colorama.Fore.LIGHTYELLOW_EX,
                                 cli_back=colorama.Back.LIGHTBLACK_EX)

        print(f'{str(player_1)} plays as white\n')
        print(f'{str(player_2)} plays as black\n')

        b = board.ChessBoard(white=player_1, black=player_2)
    else:
        player_1 = player.Player(name=p1_name, colour=chess.BLACK, cli_fore=colorama.Fore.LIGHTYELLOW_EX,
                                 cli_back=colorama.Back.LIGHTBLACK_EX)
        player_2 = player.Player(name=p2_name, colour=chess.WHITE, cli_fore=colorama.Fore.GREEN,
                                 cli_back=colorama.Back.WHITE)

        print(f'{str(player_1)} plays as black\n')
        print(f'{str(player_2)} plays as white\n')

        b = board.ChessBoard(white=player_2, black=player_1)

    print(colorama.Style.RESET_ALL)

    # Initialise file to keep track of the board and each move
    f = f'{b.white.name}_vs_{b.black.name}_{time.strftime("%d_%m_%Y_%H_%M_%S")}.txt'

    utils.io.initialise_file(
        file_name=f,
        board=b)

    inp = ''
    current_player = b.white

    # main game loop
    while not inp == 'q':
        # clear terminal before printing the board (works on Windows and Unix systems)
        os.system('cls' if os.name == 'nt' else 'clear')

        b.print()
        move, b = play_turn(p=current_player, b=b, file_name=f)

        if current_player == b.white:
            current_player = b.black
        else:
            current_player = b.white

        inp = move

    print('\nBye\n')
    sys.exit(0)
