#!/usr/bin/python3
def search_replace(my_list, search, replace):
    while (my_list.count(search)):
        my_list[my_list.index(search)] = replace
