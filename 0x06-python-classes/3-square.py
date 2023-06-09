#!/usr/bin/python3

"""class Square."""


class Square:
    """a square."""

    def __init__(self, size=0):
        """ initialize a new one (square)
        takes arg:
        size which is int and size of new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)
