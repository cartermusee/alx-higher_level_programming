#!/usr/bin/python3
"""module for class basegeo"""


class BaseGeometry:
    """a class with method area"""
    def area(self):
        """function wich raises error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.value))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.value))
