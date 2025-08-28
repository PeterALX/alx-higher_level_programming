#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    argsLength = len(args) - 1
    if argsLength == 0:
        print('0 arguments.')
    elif argsLength == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(argsLength))
    for idx, arg in enumerate(args):
        if (idx > 0):
            print('{}: {}'.format(idx, arg))
