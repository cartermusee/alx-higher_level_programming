#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:

    """ class rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        """ Instantiation with width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of height"""
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
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)])
            for j in range(self.__height)]))

    def __repr__(self):
        """ return string rep of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
