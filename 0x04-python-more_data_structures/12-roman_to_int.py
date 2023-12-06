#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    c = 0
    while c < len(roman_string):
        if (
            c + 1 < len(roman_string)
            and rom_num[roman_string[c]] < rom_num[roman_string[c + 1]]
        ):
            num -= rom_num[roman_string[c]]
        else:
            num += rom_num[roman_string[c]]
        c += 1
    return num
