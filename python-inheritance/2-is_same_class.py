#!/usr/bin/python3
"""Function return True if the object is exactly an
instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    "Simple function if object is instance of class"
    return type(obj) == a_class
