#!/usr/bin/python3
""" Defining a class module """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Integer validator
        Args:
            name (str): name of the parameter
            value (int): parameter to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
            """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
