#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    return (tuple_a[0] or 0 + tuple_b[0], tuple_a[1] + tuple_b[1])


a = 1,
print(a[0])
print(a[1])
