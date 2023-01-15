#!/usr/bin/python3


"""
This file contains a function that adds two integers
add_integer(a,b):
    adds two intgers
"""


def add_integer(a, b=98):
    """
    This function adds two integers
    Args:
        a: The first number
        b: The Scond number
    Return: The sum of the two numbers
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
