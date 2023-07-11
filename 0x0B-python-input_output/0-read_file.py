#!/usr/bin/python3
"""module with read function"""


def read_file(filename = ""):
    """function which reads a file"""
    with open(filename, encoding = 'utf-8') as f:
        print(f.read())

