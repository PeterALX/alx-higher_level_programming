#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    args = sys.argv

    count = 1
    sum = 0
    while count < len(args):
        number = int(args[count])
        sum += number
        count += 1
    print(sum)
