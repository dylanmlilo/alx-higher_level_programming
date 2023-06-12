#!/usr/bin/python3
""" Defining a class module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from BaseGeometry """
    def __init__(self, size):
        """ Initialising the  size of the square
         Args:
            size (int): the size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Computes the Area of a square """
        return (self.__size ** 2)

    def __str__(self):
        """ str for printing """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
