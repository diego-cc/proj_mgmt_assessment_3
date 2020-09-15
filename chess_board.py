"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 15/09/2020 5:01 pm
File: chess_board.py
"""
import string
from chess_pieces import ChessPieces


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
    def board(self):
        return self.__positions

    @property
    def initial_state(self):
        return self.__initial_state

    def print_state(self):
        print('\t', end="", flush=True)
        for p in range(8):
            print(string.ascii_letters[p] + '  ', end="", flush=True)
        print('\t', end="", flush=True)
        print("\n")
        # print each row
        print(f'\t')

    def map_pieces_to_positions(self, pos: str):
        pass
