#!/usr/bin/python3
"""
creat new class inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """creat Rectangle class inherits from BaseGeo"""

    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """implment area"""

        return self.__height * self.__width

    def __str__(self):
        """return a description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
