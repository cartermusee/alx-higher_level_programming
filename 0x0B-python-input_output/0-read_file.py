#!/usr/bin/python3
"""module with read function"""


def read_file(filename = ""):
    """function which reads a file"""
    with open(filename, 'r',  encoding = 'utf-8') as f:
        print(f.read())

