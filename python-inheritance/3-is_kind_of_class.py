#!/usr/bin/python3
"""Function return True if the object is instance of
or if the object is an instance of a class that inherited;
otherwise False"""


def is_kind_of_class(obj, a_class):
    "Simple function if object is instance of class"
    if isinstance(obj, a_class):
        return (True)
    else:
        return(False)
