#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        sort = sorted(my_list, reverse=True)
        return(sort[0])
