#!/usr/bin/python3
"""Function return True if the object is instance of
a class  that inherited (direct or indirect from the class;
otherwise False"""


def inherits_from(obj, a_class):
    "Simple function if object is instance of class"
    current_class = type(obj)
    if isinstance(obj, a_class) and issubclass(current_class, a_class) \
            and current_class != a_class:
        return (True)
    else:
        return(False)
