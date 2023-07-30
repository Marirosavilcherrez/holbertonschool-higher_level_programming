#!/usr/bin/python3
"""Function that writes a string to a text file
(UTF8) and returns the number characters"""


def write_file(filename="", text=""):
    """Function write a text file"""
    with open(filename, "w", encoding="utf-8") as document:
        return (document.write(text))
