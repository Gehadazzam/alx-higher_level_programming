#!/usr/bin/python3
"""
Module to read from a file and print it
"""


def read_file(filename=""):
    """print frm a file"""
    with open(filename, 'r', encoding='utf-8') as my_file:
        text = my_file.read()
        print(text, end="")
