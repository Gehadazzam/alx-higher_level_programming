#!/usr/bin/python3
"""
Module to read from a file and print it
"""


def read_file(filename=""):
    """print frm a file"""
    with open(filename, "r") as my_file:
        print(my_file.read())
