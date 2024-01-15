#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def inheritance(self):
        self.assertIsInstance(Rectangle(7, 8), Base)
        r2 = Rectangle(6, 9)
        self.assertIsInstance(r2, Base)
        self.assertIsInstance(r2, Rectangle)

    def test_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(8, 7, 9, 3, 8, 5, 2)

    def test_ides(self):
        r1 = Rectangle(4, 6, 8, 4, 50)
        r2 = Rectangle(1, 3)
        r3 = Rectangle(5, 8, 7)
        r4 = Rectangle(4, 8, 5, 8, 45)
        r5 = Rectangle(8, 7, 5, 4)
        self.assertEqual(r1.id, 50)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r4.id, 45)
        self.assertEqual(r5.id, 3)

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
