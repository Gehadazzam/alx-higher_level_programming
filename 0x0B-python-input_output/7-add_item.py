#!/usr/bin/python3
"""try to add"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv = list(sys.argv[1:])

try:
    myfile = load_from_json_file("add_item.json")

except FileNotFoundError:
    myfile = []

myfile.extend(argv)
save_to_json_file(argv, "add_item.json")
