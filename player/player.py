"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 15/09/2020 5:56 pm
File: player.py
"""
import chess
import colorama


class Player:
    def __init__(self, name: str, colour: chess.Color, cli_fore: int = None, cli_back: int = None):
        self.__name = name
        self.__colour = colour
        self.__pieces_taken = []
        self.__cli_fore = cli_fore
        self.__cli_back = cli_back

    @property
    def name(self):
        return self.__name

    @property
    def colour(self):
        return self.__colour

    @property
    def cli_fore(self):
        return self.__cli_fore

    @property
    def cli_back(self):
        return self.__cli_back

    @property
    def pieces_taken(self):
        return self.__pieces_taken

    def take_piece(self, piece: chess.Piece):
        self.__pieces_taken.append(piece)

    def __str__(self):
        return f'{self.__cli_fore}{self.__cli_back}{self.__name}{colorama.Style.RESET_ALL}'

    def print_name_and_colour(self):
        if self.__colour == 0:
            return f'{self.__name} (Black)'
        return f'{self.__name} (White)'
