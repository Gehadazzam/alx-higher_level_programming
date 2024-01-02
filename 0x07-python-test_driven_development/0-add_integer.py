#!/usr/bin/python3
def add_integer(a, b=98):
    """add two numbers.
    Parameters:
    a: int or float
    b: int or float, bu dafult = 98

    Return:
    the integer which sum a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
