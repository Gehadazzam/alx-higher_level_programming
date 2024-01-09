#!/usr/bin/python3
"""
Module to write in a file
"""


def write_file(filename="", text=""):
    """creat the file if it is not there"""

    with open(filename, "r", encoding="utf-8") as myfile:
        return myfile.write(text)
