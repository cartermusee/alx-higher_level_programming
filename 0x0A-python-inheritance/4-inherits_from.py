#!/usr/bin/python3
"""module for subclass"""


def inherits_from(obj, a_class):
    """to check if subclass inherited"""
    return issubclass(ocj, a_class) and not type(obj) != a_class
