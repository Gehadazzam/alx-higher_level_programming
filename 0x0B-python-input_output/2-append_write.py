#!/usr/bin/python3
"""
Module to appened a file
"""


def append_write(filename="", text=""):
    """creat the file if it is not there"""

    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
