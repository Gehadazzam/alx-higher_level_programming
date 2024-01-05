#!/usr/bin/python3
"""
creat lockedclass
"""


class LockedClass:
    """new class prevent any one to create new
    instance attaribute unless it is first name"""

    __slots__ = ["first_name"]
