"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 11/11/2020 5:17 pm
File: cli.py
"""
from typing import Tuple
import colorama
import random
import chess
import sys
import player.player as player
import board.chess_board as board


def get_player_name(player_num: int, player_colour: int = colorama.Fore.WHITE) -> str:
    p = input(f'{player_colour}(Player {str(player_num)}) Enter your name: ')

    while not p.strip():
        print(colorama.Style.RESET_ALL)
        print('Invalid name, please try again.')
        p = input(f'{player_colour}(Player {str(player_num)}) Enter your name: ')

    print(colorama.Style.RESET_ALL)
    print()
    return p


def play_turn(p: player.Player, b: board.ChessBoard) -> Tuple[str, board.ChessBoard]:
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

    return move, b


def start():
    print('\nWelcome! This is a basic chess game.')
    print('Type "q" and press Enter anytime to quit the game.\n')

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

    inp = ''
    current_player = b.white

    # main game loop
    while not inp == 'q':
        b.print()
        move, b = play_turn(p=current_player, b=b)

        if current_player == b.white:
            current_player = b.black
        else:
            current_player = b.white

        inp = move

    print('\nBye\n')
    sys.exit(0)
