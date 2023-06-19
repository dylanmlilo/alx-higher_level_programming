#!/usr/bin/python3
""" Define square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialising a new square

        Args:
            size (int): the size of the new square
            x    (int): the x coordinate of the new square
            y    (int): the y coordinate of the new square
            id   (int): the identity of the new square

        Raises:
            TypeError: if size is not an int
            ValueError: if size <= 0
            TypeError: if x or y is not an int
            ValueError: if x or y < 0
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the size of the new square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size of the new square """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ updates object attributes """
        attr = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
