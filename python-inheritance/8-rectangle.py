#!/usr/bin/python3
"""This is a module for Rectangle that inherits from class
BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """This is a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """This is a constructor.
        Arg:
            widht: of the rectangle
            height: of the rectangle
            """      
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

