#!/usr/bin/python3
"""
check if object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    return true or false
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
