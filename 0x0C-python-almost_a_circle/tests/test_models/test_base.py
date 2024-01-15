#!/usr/bin/python3
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):

        rectangle = Base()
        self.assertEqual(rectangle.id, 1)

        rectangle = Base(98)
        self.assertEqual(rectangle.id, 98)

        rectangle = Base()
        self.assertEqual(rectangle.id, 2)

        base = Base(98)
        base.id = 70
        self.assertEqual(base.id, 70)

        self.assertEqual("test", Base("test").id)
        self.assertEqual(45.7, Base(45.7).id)

        with self.assertRaises(TypeError):
            base = Base(5, 8)

    def test_ides(self):
        b1 = Base(67)
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 67)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

    def test_to_json(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        list = [{"id": 4}, {"id": 6}]
        json_string = '[{"id": 4}, {"id": 6}]'
        self.assertEqual(Base.to_json_string(list), json_string)


    def test_error(self):
        with self.assertRaises(AttributeError):
            Base.__nb_objects

if __name__ == "__main__":
    unittest.main()
