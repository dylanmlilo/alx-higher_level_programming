#!/usr/bin/python3
""" Defines a lookup module """


def lookup(obj):
    """
    function that looks up the available attributes and methods of an object

    Args:
        obj: object to look up

    Return:
        the list of available attributes and methods of an object
    """
    return dir(obj)
