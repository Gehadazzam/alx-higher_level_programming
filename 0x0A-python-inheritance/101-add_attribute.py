#!/usr/bin/python3
"""
Module to add attribute
"""


def add_attribute(obj, attr, value):
    """raise an error if we can add new one"""
    if isinstance(obj, (int, float, str, bool, type(None))):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
