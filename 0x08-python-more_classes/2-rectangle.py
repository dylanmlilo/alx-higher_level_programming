#!/usr/bin/python3
""" Defining a Class Rectangle """


class Rectangle:
    """ Class Rectangle """
    def __init__(self, width=0, height=0):
        """ Initialising a new Rectangle
        Args:
            width (int): the width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the current width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set the width of the rectangle """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the current height of the rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set the height of the rectangle """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))
