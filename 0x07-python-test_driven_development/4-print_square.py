#!/usr/bin/python3
"""

Module for print a square

"""


def print_square(size):
    """print a square with an integer parameter called size
    Return: error massage or square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size, end="")
        print()
