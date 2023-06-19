#!/usr/bin/python3
""" Define  a class module"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialising a new rectangle

        Args:
            width  (int): the width of the rectangle
            height (int): the height of the rectangle
            x      (int): the x cordinate of the rectangle
            y      (int): the y cordinate of the rectangle
            id     (int): the identity of the rectangle

        Raises:
            TypeError: if width or height is not an int
            ValueError: if width or height <= 0
            TypeError: if x or y is not an int
            ValueError: if x or y < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get the x cordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x cordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get the y cordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y cordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """

        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end='')
            for h in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ overriding the __str__ method so that it returns
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        Args:
            args: arguments for values of class attributes
            kwargs: dictionary containing attributes and their values
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary representation of a rectangle """
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
