#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cn, column in enumerate(row):
            end = '' if cn == len(row) - 1 else ' '
            print('{:d}'.format(column), end=end)
        print()
