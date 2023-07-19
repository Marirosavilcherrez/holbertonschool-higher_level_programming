#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for index, i in enumerate(new_list):
        if i == search:
            new_list[index] = replace
    return (new_list)
