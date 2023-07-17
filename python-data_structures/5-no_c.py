#!/usr/bin/python3
def no_c(my_string):
    letters = "Cc"
    new_string = my_string.translate(str.maketrans('', '', letters))
    return (new_string)
