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
    """This class keeps track of the current state of the board, including retrieving pieces, making moves and
    printing to the terminal."""

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
        """Retrieves a piece from a certain `square`.

        :param square: String representation of a square in the board (e.g. a2, e5, etc.)
        :return: Piece found at the specified `square` or None if not found
        """
        return self.__board.piece_at(chess.Square(square))

    def move_piece(self, uci_move: str) -> bool:
        """Validates and moves a piece based on the specified `uci_move`.

        :param uci_move: String representation of a UCI move. It consists of a "from" position and a "to" position concatenated together, without spaces. For instance, a starting move for white could be `f2f4`, where a white pawn moves from the f2 square to f4.
        :return: Whether the move is legal. If so, it gets pushed into the moves stack of the board and its state is updated.
        """
        if len(uci_move) < 4 or len(uci_move) > 5:
            return False

        try:
            m = chess.Move.from_uci(uci_move)

            if self.__board.is_castling(move=m):
                print('This is a castling move\n')

            if m in self.board.legal_moves:
                self.board.push(m)
                return True
        except:
            pass

        return False

    def print(self):
        """Prints the current state of the board, along with the name of each player."""

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
        """Prints files of the board (columns with letters `a` to `h`)"""

        print("\n")
        print(" " * 6, end="", flush=True)
        for p in range(8):
            print(string.ascii_letters[p] + " ", end="", flush=True)
        print("\n")

    @staticmethod
    def __print_ranks(ranks: List[str]):
        """Prints ranks of the board (rows with numbers `8` to `1`, along with pieces separated by spaces).

        :param ranks: Ranks retrieved from the current state of the board
        :return: String representation of the ranks
        """
        for r in range(len(ranks)):
            pieces = ranks[r].split(" ")
            # prepend rank
            pieces.insert(0, str(8 - r) + " " * 4)
            # append rank
            pieces.append(" " * 4 + str(8 - r))
            ranks[r] = " ".join(pieces)
        return ranks
