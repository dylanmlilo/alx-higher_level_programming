#!/usr/bin/python3
"""Define square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """
        Initializes the attributes of a Square instance
        Args:
        size: (int) value of size attribute
        """
        self.size = size

    @property
    def size(self):
        """set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the size square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes the area of a Square object"""
        return self.__size ** 2
