#!/usr/bin/python3
for number in range(10):
    for num in range(number + 1, 10):
        end = ", " if not (number == 8 and num == 9) else "\n"
        print("{}{}".format(number, num), end=end)
