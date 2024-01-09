#!/usr/bin/python3
"""load from file importing json"""


import json


def load_from_json_file(filename):
    """useing with and json to load from a file"""

    with open(filename, "r", encoding='utf-8') as myfile:
        json.load(myfile)
