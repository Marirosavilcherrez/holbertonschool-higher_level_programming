#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    multi = list(map(lambda x: x * number, new_list))
    return (multi)
