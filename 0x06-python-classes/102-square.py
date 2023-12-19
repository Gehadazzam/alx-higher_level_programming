#!/usr/bin/python3
"""
creat new class
named Square
"""


class Square:
    """define private attribuite"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, value):
        if not isinstance(value, Square):
            return NotImplemented
        return self.area() == value.area()

    def __ne__(self, value):
        result = self.__eq__(value)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, value):
        if not isinstance(value, Square):
            return NotImplemented
        return self.area() < value.area()

    def __le__(self, value):
        if not isinstance(value, Square):
            return NotImplemented
        return self.area() <= value.area()

    def __gt__(self, value):
        if not isinstance(value, Square):
            return NotImplemented
        return self.area() > value.area()

    def __ge__(self, value):
        if not isinstance(value, Square):
            return NotImplemented
        return self.area() >= value.area()
