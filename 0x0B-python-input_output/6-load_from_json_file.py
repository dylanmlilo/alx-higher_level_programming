#!/usr/bin/python3
""" Defining a function module """
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename) as file:
        return json.load(file)
