#!/usr/bin/python3
"""module to create a write function"""


def write_file(filename="", text=""):
    """function for writing a file"""

    with open(filename, 'w', encoding="utf-8") as f:
        print(f.write(text), end='')
