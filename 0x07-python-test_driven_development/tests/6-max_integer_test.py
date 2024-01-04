#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_argument(self):
        self.assertEqual(max_integer([4, 7, 9]), 9)
    
    def test_negativenum(self):
       self.assertEqual(max_integer([-9, -100, -1]), -1)

    def zero_test(self):
       self.assertEqual(max_integer([-90, -6, 0]), 0)
       self.assertEqual(max_integer([4, 0, 9]), 9)

    def None_test(self):
        self.assertEqual(max_integer([]), None)

    def type_error_test(self):
        self.assertEqual(TypeError, max_integer(["Gehad", 1]))
        self.assertEqual(TypeError, max_integer(102))
        self.assertEqual(TypeError, max_integer({6, 8, 9}))
        self.assertEqual(TypeError, max_integer([1, [7, 6]]))
        self.assertEqual(TypeError, max_integer("hi"))
       

