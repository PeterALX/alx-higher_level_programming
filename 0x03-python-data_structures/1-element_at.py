#!/usr/bin/python3
def element_at(my_list, idx):
    res = None
    if (idx >= 0 and idx > len(my_list)):
        res = my_list[idx]
    return res
