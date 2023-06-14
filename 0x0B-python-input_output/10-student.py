#!/usr/bin/python3
""" Define  a class module"""


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """ Initialising a new Student

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
