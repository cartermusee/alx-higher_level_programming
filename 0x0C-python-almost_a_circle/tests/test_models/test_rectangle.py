#!/usr/bin/python3
"""module for rectangle class test"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """class rectaangle test"""
    def test_instance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_1arg(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_two_id_arg(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, r1.id + 1)

    def test_three_id_arg(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(3, 4, 5)
        r3 = Rectangle(2, 3, 5)
        self.assertEqual(r3.id, r2.id + 1)

    def test__id_arg(self):
        r1 = Rectangle(1, 2, 3, 5)
        r2 = Rectangle(3, 4, 4, 6)
        self.assertEqual(r2.id, r1.id + 1)

    def test_5_id_arg(self):
        r1 = Rectangle(1, 2, 4, 6, 8)
        r2 = Rectangle(3, 4, 7, 9, 9)
        self.assertEqual(r2.id, 9)

    def test_more_than_5_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__height)

    def test_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__width)

    def test_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__x)

    def test_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__y)

    def test_width_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)

    def test_height_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.height, 2)

    def test_x_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.x, 3)

    def test_y_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.y, 4)


class TestHeight(unittest.TestCase):

    """class to test height"""
    def test_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_height_turple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2))

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2])

    def test_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(1, 2))

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 3.4)

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"num1": "1", "num2": "2"})

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "r")

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


"""class to test width"""


class Testwidth(unittest.TestCase):

    """class to test width"""

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_turple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 2)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 3)

    def test_width_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1, 2), 4)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.4, 4)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"num1": "1", "num2": "2"}, 1)

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("r", 1)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 3)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)


"""test for x"""


class Testx(unittest.TestCase):

    """class to test x"""
    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_x_turple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2))

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2])

    def test_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(1, 2))

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 3.4)

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"num1": "1", "num2": "2"})

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, "r")

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 6, -2)


"""test for y"""


class Testy(unittest.TestCase):

    """class to test y"""
    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_y_turple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (1, 2))

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [1, 2])

    def test_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(1, 2))

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 3.4)

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"num1": "1", "num2": "2"})

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 3, "r")

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 6, 3, -2)


"""class to test area method"""


class TestAre(unittest.TestCase):

    """class to test area"""
    def test_all_args(self):
        r1 = Rectangle(2, 4, 0, 0, 0)
        self.assertEqual(r1.area(), 8)

    def test_all_large_args(self):
        r1 = Rectangle(23333333333333, 44444444444444)
        self.assertEqual(r1.area(), 1037037037037011851851851852)

    def test_change(self):
        r = Rectangle(2, 3)
        r.width = 3
        r.height = 5
        self.assertEqual(r.area(), 15)


"""class to test to_dict method"""


class TestDict(unittest.TestCase):

    """class to test the to_dict method"""
    def test_output(self):
        r = Rectangle(1, 2, 3, 4, 5)
        answer = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), answer)

    def test_with_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
