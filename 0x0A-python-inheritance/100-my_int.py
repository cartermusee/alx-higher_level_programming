#!/usr/bin/python3
"""module with class myint"""


class MyInt(int):
    """class myint"""
    def __eq__(self, other):
        return int(self) == int(other)

    def __ne__(self, other):
        return int(self) != int(other)
