#!/usr/bin/pthon3
"""module for checking instance"""


def is_same_class(obj, a_class):
    """check instance of a class
    args:
        obj is the instance
        a_class is the class
    Returns True of object is otherwise false"""

    return type(obj) is a_class
