#!/usr/bin/python3
""" Defining a class module """


class MyInt(int):
    """ Class MyInt"""
    def __init__(self, value):
        """ instantiates an object """
        self.value = value

    def __eq__(self, other):
        """ inverts the == operation """
        return self.value != other

    def __ne__(self, other):
        """ inverts the != operation """
        return self.value == other
