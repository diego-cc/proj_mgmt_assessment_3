"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 15/09/2020 5:13 pm
File: validation.py
"""
from typing import Dict, Union, Optional

from chess_pieces import ChessPieces


class Validation:

    @staticmethod
    def validate_move(
            piece: ChessPieces,
            board_state: Dict[str, Union[str, ChessPieces]],
            from_position: str,
            to_position: str,
            start_of_match: Optional[bool] = True
    ) -> (bool, str):
        # initial validation, verify from and to positions
        if from_position not in board_state or to_position not in board_state:
            return False, "Invalid from/to positions"

        if board_state[from_position] is None:
            return False, "No piece found in from position"

        # check piece to be moved
        piece = board_state[from_position]

        if piece == ChessPieces.BLACK_ROOK or piece == ChessPieces.WHITE_ROOK:
            if from_position[0] != to_position[0] and from_position[1] != to_position[1]:
                # rook can't move diagonally
                return False, "Illegal rook movement"

        if piece == ChessPieces.BLACK_KNIGHT or piece == ChessPieces.WHITE_KNIGHT:
            pass

        return True
