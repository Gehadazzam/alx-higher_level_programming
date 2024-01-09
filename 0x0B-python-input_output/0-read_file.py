#!/usr/bin/python3
"""
Module to read from a file and print it
"""


def read_file(filename=""):
    """print frm a file"""
    if filename:
        with open(filename, 'r', encoding='utf-8') as my_file:
            print(my_file.read())
