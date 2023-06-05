#!/usr/bin/python3
""" Defining a Class Rectangle """


class Rectangle:
    """ Class Rectangle
    Attributes:
        number_of_instances (int): the number of instances of a rectangle
        print_symbol (any): symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialising a new rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get the current width of the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set the height of the rectangle """
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
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width * 2 + self.__height))

    def __str__(self):
        """ represents the rectangle with the # character """
        if self.__width == 0 or self.__height == 0:
            return ("")

        print_rectangle = []
        for i in range(self.__height):
            [print_rectangle.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                print_rectangle.append("\n")
        return ("".join(print_rectangle))

    def __repr__(self):
        """ returns the string representation of the rectangle """
        print_rectangle = "Rectangle(" + str(self.__width)
        print_rectangle += ", " + str(self.__height) + ")"
        return (print_rectangle)

    def __del__(self):
        """ prints a message 'Bye rectangle...'
        for every deletion of a rectangle """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
