#!/usr/bin/python3
"""Function return the list of attributes and methods
of a heritance"""


class MyList(list):
    "Simple MyList class"
    def print_sorted(self):
        "Simple function sort a list"
        sorted_list = sorted(self)
        print(sorted_list)
