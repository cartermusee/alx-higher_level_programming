#!/usr/bin/python3
"""module for class"""


class Student:
    """class that defines a student """
    def __init__(self, first_name, last_name, age):
        """init func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all([type(h) == str for h in attrs]):
            return {m: n for m, n in self.__dict__.items() if m in attrs}
        else:
            return self.__dict__.copy()
