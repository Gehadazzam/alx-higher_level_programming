#!/usr/bin/python3
"""

creat class my list and it's base case list

"""


class MyList(list):
    """creat a subclass"""

    def print_sorted(self):
        """print the list sorted"""

        print(sorted(self))
