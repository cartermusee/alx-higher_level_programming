#!/usr/bin/python3
"""testing module for base with unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    """class for testing"""
    def test_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_moreinstances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_string(self):
        b1 = Base('food')
        self.assertEqual(b1.id, 'food')

    def test_float(self):
        b1 = Base(1.2)
        self.assertEqual(b1.id, 1.2)

    def test_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_arg_passed(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_after_id(self):
        b1 = Base()
        b2 = Base(3)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)

    def test_id_change(self):
        b1 = Base(12)
        b1.id = 7
        self.assertEqual(b1.id, 7)

    def test_list(self):
        b1 = Base([1, 2, 3, 'lcm'])
        self.assertEqual(b1.id, [1, 2, 3, 'lcm'])

    def test_turple(self):
        b1 = Base((1, 2, 3))
        self.assertEqual(b1.id, (1, 2, 3))

    def test_dict(self):
        b1 = Base({'num1': "2", "num2": "3"})
        self.assertEqual(b1.id, {'num1': "2", "num2": "3"})

    def test_complex(self):
        b1 = Base(complex(2))
        self.assertEqual(b1.id, complex(2))

    def test_bool(self):
        b1 = Base(False)
        self.assertEqual(b1.id, False)

    def test_more_arg(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_print_private_attr(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)


class TestBase_to_json(unittest.TestCase):
    """class to test the base method to json"""
    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(type(Base.to_json_string([r.to_dictionary()])), str)

    """def test_str_square(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(type(Base.to_json_string([s.to_dictionary])))"""

    """def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')"""

    def test_none_empty_list(self):
        self.assertEqual(Base.to_json_string([None]), '[null]')

    def test_more_than_one(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


if __name__ == '__main__':
    unittest.main()
