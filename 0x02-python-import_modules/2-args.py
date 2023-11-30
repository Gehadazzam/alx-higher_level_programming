#!/usr/bin/python3
if __name__ == "__main__":
    """print the sum of 1 and 2"""
import sys
argc = len(sys.argv) - 1
arguments = sys.argv[1:]
if argc == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(argc))
    for item in range(argc):
        print("{}: {}".format(item+1, arguments[item]))
