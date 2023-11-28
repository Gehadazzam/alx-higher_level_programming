#!/usr/bin/python3
for number in range(100):
    if number < 10:
        print("0{}".format(number), end=", ")
    else:
        print("{}".format(number), end=", ")
        if number == 99:
            print('\n')
