#!/usr/bin/python3
"""write to file importing json"""


import json


def save_to_json_file(my_obj, filename):
    """useing with and json to write to a file"""

    with open(filename, "w", encoding='utf-8') as myfile:
        json.dump(my_obj, myfile)
