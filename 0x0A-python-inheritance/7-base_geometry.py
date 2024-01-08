#!/usr/bin/python3
"""
creat a base geo class
"""


class BaseGeometry:
    """init the class"""

    def area(self):
        """ just type massage"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate a value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
