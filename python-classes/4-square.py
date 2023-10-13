#!/usr/bin/python3
"""This module has a class that defines a square"""


class Square:
    """Definition of square attribute"""

    def __init__(self, size=0):
        """Initialize"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Return square area"""
        square_area = self.__size ** 2
        return square_area
