#!/usr/bin/python3
"""
Module to add attribute
"""


def add_attribute(obj, attr, value):
    """raise an error if we can add new one"""
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, attr)
