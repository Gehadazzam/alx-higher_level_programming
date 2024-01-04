#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for word in text:
        print(word, end='')
        if word in ['.', '?', ':']:
            print("\n\n", end='')
