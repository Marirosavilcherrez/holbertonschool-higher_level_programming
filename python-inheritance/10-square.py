#!/usr/bin/python3
"""This is a module for Square that inherits from class
Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """This is a constructor.
        Arg:
        size: of the rectangle"""
        super().__init__(size, size)
