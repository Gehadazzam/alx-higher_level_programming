#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
total = 0
if argc == 0:
    print(0)
else:
    for item in range(1, argc + 1):
        arguments = int(sys.argv[item])
        total += arguments
    print("{}".format(total))
