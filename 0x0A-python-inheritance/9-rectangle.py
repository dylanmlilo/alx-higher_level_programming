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
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ computes the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """str method for printing"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
