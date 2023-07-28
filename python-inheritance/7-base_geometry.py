#!/usr/bin/python3
"""Write a class BaseGeometry, public instance method,
area and integer_validator"""


class BaseGeometry:
    """Simple BaseGeometry class"""
    pass

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
