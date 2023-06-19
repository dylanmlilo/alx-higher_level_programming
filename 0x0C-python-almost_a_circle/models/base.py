#!/usr/bin/python3
""" Defining a Class module """

import json
import csv


class Base:
    """ Class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialising a new base
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
