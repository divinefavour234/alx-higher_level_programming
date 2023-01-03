#!/usr/bin/python3
"""
This module contains some class
"""


class Square:
    """
    This class contains some functions
    """
    def __init__(self, size=0):
        """
        param1 (int): The first parameter which is optional
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
