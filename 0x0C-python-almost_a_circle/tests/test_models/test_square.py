#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_id(self):
        s1 = Square(6, 7, 8, 34)
        s4 = Square(4, 8, 5, 40)

        self.assertEqual(s1.id, 34)
        self.assertEqual(s4.id, 40)
        self.assertEqual(s1.y, 8)

        s7 = Square(8, 6)
        s8 = Square(6, 4)
        self.assertEqual(s7.id, s8.id - 1)
        self.assertEqual(s7.size, 8)
        self.assertEqual(s8.x, 4)

        s1.size = 23
        self.assertEqual(s1.size, 23)

    def inheritance(self):
        self.assertIsInstance(Square(9), Base)

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
