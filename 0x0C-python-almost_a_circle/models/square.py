#!/usr/bin/python3
"""creating class Square wich will be inherited
    from Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """creat the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init the variables"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a statment about the square"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    """set the size"""

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the variables"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """print the variables in a dictonary"""

        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
