#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if i != j and j > i:
            if (i != 8):
                print("{}, ".format(str(i)+str(j)))
            else:
                print("{}".format(str(i)+str(j)), end='')
