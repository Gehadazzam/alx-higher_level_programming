#!/usr/bin/python3
import unittest
import json

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

    def test_to_json(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        list = [{"id": 4}, {"id": 6}]
        json_string = '[{"id": 4}, {"id": 6}]'
        self.assertEqual(Base.to_json_string(list), json_string)


if __name__ == "__main__":
    unittest.main()