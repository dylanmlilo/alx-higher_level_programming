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
