#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def inheritance(self):
        self.assertIsInstance(Rectangle(7, 8), Base)

    def test_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(8, 7, 9, 3, 8, 5, 2)

    def test_more_args(self):

        rec = Rectangle(4, 2, 6)
        self.assertEqual(rec.y, 0)

        rec = Rectangle(7, 8, 9, 4)
        rec1 = Rectangle(6, 8)
        self.assertEqual(rec.id, rec1.id - 1)

        rec = Rectangle(8, 4)
        self.assertEqual(rec.x, 0)



if __name__ == "__main__":
    unittest.main()
