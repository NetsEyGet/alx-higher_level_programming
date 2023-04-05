#!/usr/bin/python3
"""
This function is used to add two integers
"""


def add_integer(a, b=98):
    """
    This mathod raises error if it is not integer or float
    Args: a: The fist number to be added
          b: The second number to be added
    Return: returns the sum of both number
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
