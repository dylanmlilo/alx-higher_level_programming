#!/usr/bin/python3
""" Defining a class module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Initialising the width and height
         Args:
            width (int): the width of the new Rectangle
            height (int): the height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
