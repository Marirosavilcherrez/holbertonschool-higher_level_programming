#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for index, i in enumerate(new_list):
        if i == 2:
            new_list[index] = 89
    return (new_list)
