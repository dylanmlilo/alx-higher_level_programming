#!/usr/bin/python
"""Define Square. Module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialisinge a new square.
        """
        self.size = size

    @property
    def size(self):
        """get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """det the size ofthe square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """compute the area of the square."""
        return (self.__size ** 2)

    def __lt__(self, val):
        """less than check"""
        return self.area() < val.area()

    def __le__(self, val):
        """less than equal to check"""
        return self.area() <= val.area()

    def __eq__(self, val):
        """equal to check"""
        return self.area() == val.area()

    def __ne__(self, val):
        """not equal to check"""
        return self.area() != val.area()

    def __gt__(self, val):
        """greater than check"""
        return self.area() > val.area()

    def __ge__(self, val):
        """greater than or equal to check"""
        return self.area() >= val.area()
