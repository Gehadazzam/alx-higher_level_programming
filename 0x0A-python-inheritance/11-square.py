#!/usr/bin/python3
"""
creat a square class inheirts from Rectangle class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """new class inherits from Rectangle class"""

    def __init__(self, size):
        """init the size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """return a description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
