#!/usr/bin/python3
"""module for class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class which inherits from class rectangle"""
    def __init__(self, size):
        """function for variables"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return area"""
        return self.__size ** 2

    def __str__(self):
        """string repre"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
