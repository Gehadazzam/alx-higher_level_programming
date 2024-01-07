#!/usr/bin/python3
"""

Module for print 2 new lines after a sentense

"""


def text_indentation(text):
    """
    return a text following by 2 black line after . or ? with one parameter
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for word in text:
        print(word, end="")
        if word in [".", "?", ":"]:
            print("\n\n", end="")
