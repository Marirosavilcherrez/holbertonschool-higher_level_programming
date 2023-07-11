#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if (number < 0) and (lastdig != 0):
    print(F"Last digit of {number} is -{lastdig} and is less than 6 and not 0")
elif lastdig > 5:
    print(F"Last digit of {number} is {lastdig} and is greater than 5")
elif lastdig == 0:
    print(F"Last digit of {number} is {lastdig} and is 0")
elif (0 < lastdig < 6):
    print(F"Last digit of {number} is {lastdig} and is less than 6 and not 0")
