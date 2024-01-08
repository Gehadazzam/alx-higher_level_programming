#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
creat new class inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """creat Rectangle class inherits from BaseGeo"""

    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width
