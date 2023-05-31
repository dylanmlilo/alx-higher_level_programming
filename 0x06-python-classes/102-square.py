#!/usr/bin/python3
"""Define a Square module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialising a new square
        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square"""
        return (self.__size ** 2)

    def __eq__(self, content):
        """Define the == comparision"""
        return self.area() == content.area()

    def __ne__(self, content):
        """Define the != comparison"""
        return self.area() != content.area()

    def __lt__(self, content):
        """Define the < comparison"""
        return self.area() < content.area()

    def __le__(self, content):
        """Define the <= comparison"""
        return self.area() <= content.area()

    def __gt__(self, content):
        """Define the > comparison"""
        return self.area() > content.area()

    def __ge__(self, content):
        """Define the >= compmarison"""
        return self.area() >= content.area()
