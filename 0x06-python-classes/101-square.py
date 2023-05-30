#!/usr/bin/python
"""Define square module"""\


class Square():
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get position the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position the of square """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes the area of a Square object"""
        return self.__size ** 2

    def my_print(self):
        """ prints a square """
        if self.__size <= 0:
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size, end="")
            if _ < self.__size - 1:
                print()

    def __str__(self):
        """ ensures that Square instance should
        have the same behavior as my_print()
        """
        self.my_print()
        return ""
