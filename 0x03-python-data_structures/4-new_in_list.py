#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list.copy()
    if idx < 0 or idx >= len(a):
        return(a)
    a[idx] = element
    return(a)
