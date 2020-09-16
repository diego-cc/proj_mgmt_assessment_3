"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 15/09/2020 5:01 pm
File: chess_board.py
"""
import string
from typing import Optional, List

import chess


class ChessBoard:
    def __init__(self, initial_state: Optional[str] = None):
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

    def move_piece(self, uci_move: str) -> bool:
        m = chess.Move.from_uci(uci_move)
        if m in self.board.legal_moves:
            self.board.push(m)
            return True
        return False

    def print(self):
        ChessBoard.__print_files()
        b = str(self.__board)
        ranks = b.split("\n")

        numbered_ranks = ChessBoard.__print_ranks(ranks)

        b_to_str = "\n".join(numbered_ranks)
        print(b_to_str, end="", flush=True)
        ChessBoard.__print_files()

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


"""
Initial approach, implementing a chess board class from scratch

class ChessBoard:
    __initial_state = {
        "a1": ChessPieces.WHITE_ROOK,
        "b1": ChessPieces.WHITE_KNIGHT,
        "c1": ChessPieces.WHITE_BISHOP,
        "d1": ChessPieces.WHITE_QUEEN,
        "e1": ChessPieces.WHITE_KING,
        "f1": ChessPieces.WHITE_BISHOP,
        "g1": ChessPieces.WHITE_KNIGHT,
        "h1": ChessPieces.WHITE_ROOK,
        "a2": ChessPieces.WHITE_PAWN,
        "b2": ChessPieces.WHITE_PAWN,
        "c2": ChessPieces.WHITE_PAWN,
        "d2": ChessPieces.WHITE_PAWN,
        "e2": ChessPieces.WHITE_PAWN,
        "f2": ChessPieces.WHITE_PAWN,
        "g2": ChessPieces.WHITE_PAWN,
        "h2": ChessPieces.WHITE_PAWN,
        "a3": ".",
        "b3": ".",
        "c3": ".",
        "d3": ".",
        "e3": ".",
        "f3": ".",
        "g3": ".",
        "h3": ".",
        "a4": ".",
        "b4": ".",
        "c4": ".",
        "d4": ".",
        "e4": ".",
        "f4": ".",
        "g4": ".",
        "h4": ".",
        "a5": ".",
        "b5": ".",
        "c5": ".",
        "d5": ".",
        "e5": ".",
        "f5": ".",
        "g5": ".",
        "h5": ".",
        "a6": ".",
        "b6": ".",
        "c6": ".",
        "d6": ".",
        "e6": ".",
        "f6": ".",
        "g6": ".",
        "h6": ".",
        "a7": ChessPieces.BLACK_PAWN,
        "b7": ChessPieces.BLACK_PAWN,
        "c7": ChessPieces.BLACK_PAWN,
        "d7": ChessPieces.BLACK_PAWN,
        "e7": ChessPieces.BLACK_PAWN,
        "f7": ChessPieces.BLACK_PAWN,
        "g7": ChessPieces.BLACK_PAWN,
        "h7": ChessPieces.BLACK_PAWN,
        "a8": ChessPieces.BLACK_ROOK,
        "b8": ChessPieces.BLACK_KNIGHT,
        "c8": ChessPieces.BLACK_BISHOP,
        "d8": ChessPieces.BLACK_QUEEN,
        "e8": ChessPieces.BLACK_KING,
        "f8": ChessPieces.BLACK_BISHOP,
        "g8": ChessPieces.BLACK_KNIGHT,
        "h8": ChessPieces.BLACK_ROOK
    }
    def __init__(self):
        rows, cols = (8, 8)
        positions = [[string.ascii_letters[i] + str(j + 1) for i in range(cols)] for j in range(rows)]
        self.__positions = positions

    @property
    def positions(self):
        return self.__positions

    @property
    def initial_state(self):
        return self.__initial_state

    @staticmethod
    def print_letters():
        print(" " * 5, end="", flush=True)
        for p in range(8):
            print(string.ascii_letters[p] + "  ", end="", flush=True)
        print(" " * 4, end="", flush=True)
        print("\n")

    def print_state(self, state: Dict[str, Union[str, ChessPieces]] = __initial_state):
        ChessBoard.print_letters()
        # print each row
        for r in range(8, 0, -1):
            print(r, end="", flush=True)
            print(" " * 4, end="", flush=True)
            for c in string.ascii_lowercase[:8]:
                key = c + str(r)
                if str(state[key]) == state[key]:
                    if c != "h":
                        print(state[key] + "  ", end="", flush=True)
                    else:
                        print(state[key], end="", flush=True)
                        print(" " * 4, end="", flush=True)
                else:
                    if c != "h":
                        print(state[key].value + "  ", end="", flush=True)
                    else:
                        print(state[key].value, end="", flush=True)
                        print(" " * 4, end="", flush=True)

            print(str(r), end="", flush=True)
            print()
        print()
        ChessBoard.print_letters()
"""
