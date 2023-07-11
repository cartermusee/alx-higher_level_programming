#!/usr/bin/python3
"""module for append function"""


def append_write(filename="", text=""):
    """function to append
    returns nmber of chars"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
