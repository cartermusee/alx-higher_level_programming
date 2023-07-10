#!/usr/bin/python3
"""module with class which inherits"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle which nherits geometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """the area"""
        return self.__width * self.__height

    def __str__(self):
        """string repre"""
        return "[Rectangle]" + \str(self.__width) + "/" + str(self.__height)
