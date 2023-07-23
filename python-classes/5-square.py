#!/usr/bin/python3
"""A class Square that defines a square"""
"""This is a module of square"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0):
        """This is a constructor.
        Arguments:
        Size: side of square"""
        self.__size = size

    @property
    def size(self):
        """There are a getter and setter when to get/set
        the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """This method returns the stdout the square character"""
        character = "#"
        size_1 = self.__size
        if size_1 == 0:
            print("")
        else:
            for j in range(size_1):
                for i in range(size_1):
                    print("{}".format(character), end="")
                print("")
