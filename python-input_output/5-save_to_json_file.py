#!/usr/bin/python3
"""Function that returns an object Object to a text
file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function return JSON"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
