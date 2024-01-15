#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70), Square(24), Square(70)]

    Base.draw(list_rectangles, list_squares)

    list = [Rectangle(20,40), Rectangle(60,80), Rectangle(30, 50)]
    list_2 = [Square(30), Square(70), Square(45)]
    Base.draw(list_2, list)