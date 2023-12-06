#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    item = 0
    while item < len(roman_string):
        if (
            item + 1 < len(roman_string)
            and roman_num[roman_string[item]] < roman_num[roman_string[item + 1]]
        ):
            num -= roman_num[roman_string[item]]
        else:
            num += roman_num[roman_string[item]]
        item += 1
    return num
