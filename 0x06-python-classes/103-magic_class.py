#!/usr/bin/python3

import math


class MagicClass:
    """An implementation of the MagicClass disassembly"""

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of the square instance"""
        return self.__radius ** 2 * math.pi

    def circumfrence(self):
        """Returns the circumfrence of the square instance"""
        return 2 * math.pi * self.__radius
