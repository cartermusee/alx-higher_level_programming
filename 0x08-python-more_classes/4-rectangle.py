#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """ class rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width"""
        return self.__width

    @property
    def height(self):
        """ height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimiter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return rectangle with the character #"""
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """ return string rep of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
