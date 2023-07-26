#!/usr/bin/python3
"A class Rectangle that defines a rectangle"
"""This is a module of rectangle"""


class Rectangle:
    "Simple Rectangle class"
    def __init__(self, width=0, height=0):
        """This is a constructor.
        Args:
        Size: side of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Propertie to retrieve it"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Class methods are similar to regular functions.

        Args:
            param1: value.

        Returns:
            True if successful, False otherwise.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Propertie to retrieve it"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Class methods are similar to regular functions.

        Args:
            param1: value.

        Returns:
            True if successful, False otherwise.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
