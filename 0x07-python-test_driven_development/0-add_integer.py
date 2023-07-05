#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function that adds two integers
a and b must be integers or floats
Raise a TypeError exception otherwise
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """eturns an integer: the addition of a and b
    If a or b is an float, it must be typecasted to an int before adding
    Raises: TypeError if a or b is neither an int nor a float"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
