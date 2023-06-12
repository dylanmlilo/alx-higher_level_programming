#!/usr/bin/python3
""" Define a class module """


class MyList(list):
    """ prints a list in sorted ascending order """
    def print_sorted(self):
        """ print a list in sorted ascending order """
        print(sorted(self))
