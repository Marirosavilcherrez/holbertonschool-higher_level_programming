#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        if count < x:
            try:
                print("{:d}".format(i), end='')
            except IndexError:
                pass
        else:
            break
        count += 1
    print('')
    return (count)
