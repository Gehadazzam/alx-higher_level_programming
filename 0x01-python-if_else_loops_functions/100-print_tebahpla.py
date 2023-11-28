#!/usr/bin/python3
for alpha in range(122, 96, -1):
    case = 'lower' if alpha % 2 == 1 else 'upper'
    print("{}".format(
        chr(alpha).upper() if case == 'lower' else chr(alpha)), end='')
