#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    i = 0
    while i < list_length:
        try:
            element_1 = my_list_1[i % len(my_list_1)]
            element_2 = my_list_2[i % len(my_list_2)]
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                new_list[i] = 0
            elif not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                print("wrong type")
                new_list[i] = 0
            elif element_2 == 0:
                print("division by 0")
                new_list[i] = 0
            else:
                new_list[i] = element_1 / element_2
        except ZeroDivisionError:
            new_list[i] = 0
        finally:
            i = i + 1
    return (new_list)
