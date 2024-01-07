#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """This defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if the size is less than zero
        """    

        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value