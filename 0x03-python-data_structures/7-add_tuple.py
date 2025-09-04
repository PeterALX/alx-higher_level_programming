#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    b = []
    for i in range(2):
        a.append(tuple_a[i] if len(tuple_a) > i else 0)
        b.append(tuple_b[i] if len(tuple_b) > i else 0)

    return (a[0] + b[0], a[1] + b[1])
