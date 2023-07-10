#!/usr/bin/python3
"""module for subclass"""


def inherits_from(obj, a_class):
    """to check if subclass inherited"""
    return isinstance(obj, a_class) and type(obj) != a_class
