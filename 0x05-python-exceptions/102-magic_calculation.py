#!/usr/bin/python3
def magic_calculation(a, b):
    calc = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            else:
                calc += (a ** b) / x
        except:
            calc = b + a
            pass
    return calc
