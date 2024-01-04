#!/usr/bin/python3
"""

Module for print names

"""


def say_my_name(first_name, last_name=""):
    """print string as names
    parameters: first name, last name: names to be printed
    Return: printed names or error"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")