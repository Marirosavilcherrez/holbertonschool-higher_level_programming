#!/usr/bin/python3
"A class Rectangle that defines a rectangle"
"""This is a module of rectangle"""


class Rectangle:
    "Simple Rectangle class"
    def __init__(self, width=0, height=0):
        """This is a constructor.

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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        width = self.width
        height = self.height
        perim = (2 * width) + (2 * height)
        if width == 0 or height == 0:
            return (0)
        else:
            return (perim)

    def __str__(self):
        width = self.width
        height = self.height
        if width == 0 or height == 0:
            return ("")
        else:
            rectangle_str = ""
            for i in range(height):
                for j in range(width):
                    rectangle_str += "#"
                rectangle_str += "\n"
            rectangle_str = rectangle_str.rstrip("\n")
            return (rectangle_str)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
