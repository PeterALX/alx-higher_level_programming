#!/usr/bin/python3

def no_c(my_string):
    string_dema_list = my_string[:]
    return ''.join(c for c in string_dema_list if c != 'c' and 'C')
