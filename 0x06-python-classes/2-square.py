#!/usr/bin/python3
"""
creat new class
named Square
"""


class Square:
    """define private attribuite"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
