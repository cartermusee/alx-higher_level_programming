#!/usr/bin/python3
"""module for list printing"""


class MyList(list):
    """class for list"""
    def print_sorted(self):
        """print sorted"""
        print(sorted(self))
