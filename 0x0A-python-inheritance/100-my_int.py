#!/usr/bin/python3
"""
new class inherits from int
"""


class MyInt(int):
    """My int class invert the true and false"""

    def __eq__(self, other):
        """True"""

        return super().__ne__(other)

    def __ne__(self, other):
        """false"""

        return super().__eq__(other)
