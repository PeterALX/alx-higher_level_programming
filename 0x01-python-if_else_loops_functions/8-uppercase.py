#!/usr/bin/python3

def uppercase(str):
    for idx, char in enumerate(str):
        if (ord(char) >= 97 and ord(char) <= 122):
            char = chr(ord(char) - 32)
        if idx == len(str) - 1:
            print(char)
        else:
            print(char, end='')
