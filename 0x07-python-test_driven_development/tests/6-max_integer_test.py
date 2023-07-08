#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test cases for the function"""

    def test_max_num(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8]), 8)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_big_num(self):
        self.assertEqual(max_integer([
            100, 200, 2, 5, 66, 78, 98,
            67, 54, 45, 23, 32, 55, 76,
            89, 65, 56]), 200)
    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([4]), 2)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_operations(self):
        self.assertEqual(max_integer([1, 3 * 4, 6, 8]), 12)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'r'])

    def test_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([1, (1, 2)])

    def test_int(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_loop(self):
        my_list = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(max_integer([j * 7 for j in my_list]), 49)
