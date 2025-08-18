#!/usr/bin/python3

def uppercase(str):
    for idx, char in enumerate(str):
        o = ord(char) - 32 if ord(char) >= 97 and ord(
            char) <= 122 else ord(char)
        if idx == len(str) - 1:
            print('{:c}'.format(o))
        else:
            print('{:c}'.format(o), end='')
