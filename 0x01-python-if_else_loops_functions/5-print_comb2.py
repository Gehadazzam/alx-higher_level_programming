#!/usr/bin/python3
for number in range(100):
    if number < 10:
        print("0{}".format(number), end=", ")
    else:
        end = ", " if number != 99 else "\n"
        print("{}".format(number), end=end)
