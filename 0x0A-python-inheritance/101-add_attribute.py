#!/usr/bin/python3
""" Defining an attribute module """


def add_attribute(obj, attr, value):
    """
    function that adds attribute to an object if it is possible

    Args:
        obj: the object to receive new attributes
        attr: the attribute name
        value: the attribute value

    Raise(s):
        TypeError: if new attribute can't be added
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
