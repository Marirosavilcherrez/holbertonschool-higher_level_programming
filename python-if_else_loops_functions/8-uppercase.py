#!/usr/bin/python3
def uppercase(str):
    newtext = ""
    for text in str:
        if ord(text) > 96 and ord(text) < 123:
            newtext += chr(ord(text) - 32)
        else:
            newtext += text
    print("{}".format(newtext))
