#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def inheritance(self):
        self.assertIsInstance(Square(7), Base)

    def test_args(self):
        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square(7, 8, 6, 5, 9, 3)

    def test_more_args(self):

        sec = Square(6)
        self.assertEqual(sec.y, 0)
        self.assertEqual(sec.x, 0)

        sec = Square(8, 7, 5)
        sec1 = Square(5, 4)
        self.assertEqual(sec.id, sec1.id - 1)


if __name__ == "__main__":
    unittest.main()
