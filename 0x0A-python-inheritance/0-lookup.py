#!/usr/bin/python3
"""module for lookup"""


def lookup(obj):
    """a function that gives available attributes
    and methods of an object

    args:
        obj which is a list
    Returns a list"""

    return dir(obj)
