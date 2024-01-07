#!/usr/bin/python3
"""

Module used to add two integers

"""


def add_integer(a, b=98):
    """add two numbers.
    Parameters: a: int or float, b: int or float, by dafult = 98
    Return: the integer which sum a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
