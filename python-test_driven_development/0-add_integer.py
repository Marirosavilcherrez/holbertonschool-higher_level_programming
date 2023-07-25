#!/usr/bin/python3
"""This is a module add integer
The module supply one function, add integers
or floats type and return an integer"""



def add_integer(a, b=98):
    """Return the sum of two integers or float,
    return integer. Otherwise TypeError"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")  
    else:
        a = int(round(a))
        b = int(round(b))
        return(a + b)
