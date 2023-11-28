#!/usr/bin/python3
for alpha in range(97, 123):
    if chr(alpha) == 'q' or chr(alpha) == 'e':
        continue;
    else:
        print(chr(alpha), end="")
