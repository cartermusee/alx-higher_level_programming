#!/usr/bin/python3
"""module for square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):

    """class square which inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        
        """constructors"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string rep"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """a getter functioin which returns the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """a setter function for size
        args:
            value which is same as size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def update(self, *args, **kwargs):
        
        """args and kwargs function
        argument:
            args:argum which are not limmited
            kwargs: defined argument"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 3:
                self.x = args[2]
            if len(args) > 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        
        """dict representation"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
