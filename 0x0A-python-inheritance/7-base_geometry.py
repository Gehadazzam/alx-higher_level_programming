#!/usr/bin/python3
"""
creat a base geo class
"""


class BaseGeometry:
    """init the class"""

    def area(self):
        """just type massage"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a value"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
