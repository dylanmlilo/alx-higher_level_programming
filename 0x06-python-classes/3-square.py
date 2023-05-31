#!/usr/bin/python3
"""Define a Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """ Initialising a new Square
        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Computes the area of a square"""
        return (self.__size ** 2)
