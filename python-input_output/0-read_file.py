#!/usr/bin/python3
"""Function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """Function text file read only"""
    with open(filename, "r", encoding="utf-8") as document:
        text = document.read()
    print(text, end="")
