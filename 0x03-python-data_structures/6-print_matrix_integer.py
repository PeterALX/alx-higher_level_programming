#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rn, row in enumerate(matrix):
        for cn, column in enumerate(row):
            end = '' if cn == len(row) - 1 else ' '
            print(column, end=end)
        print()
