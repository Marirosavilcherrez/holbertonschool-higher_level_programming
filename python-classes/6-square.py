#!/usr/bin/python3
"""A class Square that defines a square"""
"""This is a module of square"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0, position=(0, 0)):
        """This is a constructor.
        Arguments:
        Size: side of square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """There are a getter and setter when to get/set
        the current size of the square"""
        return (self.__size)

    @property
    def position(self):
        """There are a getter and setter when to get/set
        the current position of the square"""
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @size.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(val, int) for val in value) or \
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """This method returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """This method returns the stdout the square character"""
        character = "#"
        position_1 = self.__position
        size_1 = self.__size
        if size_1 == 0:
            print("")
        else:
            for i in range(position_1[1]):
                print()
            for j in range(size_1):
                for a in range(position_1[0]):
                    print("_", end="")
                for i in range(size_1):
                    print("{}".format(character), end="")
                print("")
