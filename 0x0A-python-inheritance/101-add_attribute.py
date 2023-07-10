#!/usr/bin/python3
"""module with add_attribute function"""


def add_attribute(obj, name, value):
    """function which checks for an attribute and addds it"""
    if hasattr(obj, '__dict__') or hasattr(obj, '__slots__')\
            and name in obj.__slots__:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
