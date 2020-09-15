"""
Project: proj-mgmt-assessment-3
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 15/09/2020 5:56 pm
File: player.py
"""
from colours import Colours


class Player:
    def __init__(self, name: str, colour: Colours):
        self.__name = name
        self.__colour = colour

    @property
    def name(self):
        return self.__name

    @property
    def colour(self):
        return self.__colour
