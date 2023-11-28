#!/usr/bin/python3
for number in range (100):
    if number < 10:
        print(f"0{number}", end= ", ")
    else:
        print(f"{number}", end= ", ")
        if number == 99:
            print('\n')
