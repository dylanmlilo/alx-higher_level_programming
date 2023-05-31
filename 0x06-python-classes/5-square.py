#!/usr/bin/python3
"""Define Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): The size of the new
        """
        self.size = size

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """computes the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        if self.__size <= 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
