#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.keys())
    for i in sorted_dictionary:
        print("{}: {}".format(i, a_dictionary[i]))
