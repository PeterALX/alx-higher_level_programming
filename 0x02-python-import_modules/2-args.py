#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 0:
        print('0 arguments.')
    elif len(args) == 1:
        print('1 argument:')
    else:
        print('{}'.format(len(args)))
    for idx, arg in enumerate(args):
        print('{}: {}'.format(idx, arg))
