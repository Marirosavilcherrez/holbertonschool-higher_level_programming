#!/usr/bin/python3
"""Function that appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Function append a text file"""
    with open(filename, "a", encoding="utf-8") as document:
        return (document.write(text))
