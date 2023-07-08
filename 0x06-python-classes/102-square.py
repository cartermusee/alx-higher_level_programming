#!/usr/bin/python3

"""define class square"""


class Square:

    """defines a square"""
    def __init__(self, size=0):
        """constructor.

        args:
            size:length of square
        """

        self.__size = size

    @property
    def size(self):
        """property for length of a side of square

        raises:
            typeError if size is not int
            valueError: if size less than 0
        """

        return (self.__size)
   
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of this square.
         Returns:
            The area.
        """

        return (self.__size ** 2)

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __eq__(self, other):
        return (self.area() <= other.area())

    def __ne__(self, other):
        return (self.area() <= other.area())

    def __gt__(self, other):
        return (self.area() <= other.area())

    def __ge__(self, other):
        return (self.area() <= other.area())
