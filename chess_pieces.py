"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 15/09/2020 5:06 pm
File: chess_pieces.py
"""
from enum import Enum


class ChessPieces(Enum):
    WHITE_PAWN = "P"
    BLACK_PAWN = "p"
    WHITE_ROOK = "R"
    BLACK_ROOK = "r"
    WHITE_KNIGHT = "N"
    BLACK_KNIGHT = "n"
    WHITE_BISHOP = "B"
    BLACK_BISHOP = "b"
    WHITE_QUEEN = "Q"
    BLACK_QUEEN = "q"
    WHITE_KING = "K"
    BLACK_KING = "k"
