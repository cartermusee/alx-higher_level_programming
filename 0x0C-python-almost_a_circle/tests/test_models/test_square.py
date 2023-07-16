#!/usr/bin/python3
"""module to test suare"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testsquare(unittest.TestCase):

    """Test for square"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        s1 = Square(1)
        s2 = Square(1, 2, 3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_attr(self):
        s1 = Square(1, 2, 3)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_missing(self):
        """missing arg test"""

        with self.assertRaises(TypeError) as f:
            s = Square()
            ms = "__init__() missing 1 required positional argument: 'size'"
            self.assertEqual(ms, str(f.exception))

    def test_str(self):
        """str rep"""

        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')

    def tes_update(self):
        s = Square(2)
        s.update(3)
        self.assertEqual(s.id, 3)
        s.update(size=4, x=5, y=6, id=9)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)
        self.assertEqual(s.id, 9)

    def test_to_dict(self):
        s = Square(10, 2, 1)
        s_dict = s.to_dictionary()
        answer = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(len(s_dict), len(answer))


if __name__ == '__main__':
    unittest.main()
