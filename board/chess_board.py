"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 15/09/2020 5:01 pm
File: chess_board.py
"""
import string
from typing import Optional, List

import chess
import player.player as player


class ChessBoard:
    def __init__(self, white: player.Player, black: player.Player, initial_state: Optional[str] = None):
        self.__white = white
        self.__black = black
        self.__initial_state = initial_state
        if initial_state is not None:
            self.__board = chess.Board(initial_state)
        else:
            self.__board = chess.Board()
        rows, cols = (8, 8)
        self.__positions = [[string.ascii_letters[i] + str(j + 1) for i in range(cols)] for j in range(rows)]

    @property
    def positions(self):
        return self.__positions

    @property
    def initial_state(self):
        return self.__initial_state

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, b: chess.Board):
        self.__board = b

    @property
    def white(self):
        return self.__white

    @property
    def black(self):
        return self.__black

    def get_piece_at(self, square: str) -> Optional[chess.Piece]:
        return self.__board.piece_at(chess.Square(square))

    def move_piece(self, uci_move: str) -> bool:
        if len(uci_move) < 4 or len(uci_move) > 5:
            return False

        m = chess.Move.from_uci(uci_move)
        if m in self.board.legal_moves:
            self.board.push(m)
            return True
        return False

    def print(self):
        print(" " * 12, end="", flush=True)
        print(str(self.__black))

        ChessBoard.__print_files()
        b = str(self.__board)
        ranks = b.split("\n")

        numbered_ranks = ChessBoard.__print_ranks(ranks)

        b_to_str = "\n".join(numbered_ranks)
        print(b_to_str, end="", flush=True)
        ChessBoard.__print_files()

        print(" " * 12, end="", flush=True)
        print(str(self.__white))

    @staticmethod
    def __print_files():
        print("\n")
        print(" " * 6, end="", flush=True)
        for p in range(8):
            print(string.ascii_letters[p] + " ", end="", flush=True)
        print("\n")

    @staticmethod
    def __print_ranks(ranks: List[str]):
        for r in range(len(ranks)):
            pieces = ranks[r].split(" ")
            # prepend rank
            pieces.insert(0, str(8 - r) + " " * 4)
            # append rank
            pieces.append(" " * 4 + str(8 - r))
            ranks[r] = " ".join(pieces)
        return ranks
