#!/usr/bin/python3
"A class Square that defines a square"
"Private instance attribute size"


class Square:
    "Instantiation with size"
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except Exception:
            pass
