#!/usr/bin/python3
"""
Module to get the atrribuites
"""


def lookup(obj):
    """
    return a list of attributes and methodes of a class
    """
    return [attribute for attribute in dir(obj)]
