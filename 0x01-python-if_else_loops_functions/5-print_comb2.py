#!/usr/bin/python3
for i in range(0, 100):
    if i // 10 == 0:
        print('0', end='')
    if i == 99:
        print('{}'.format(i))
    else:
        print('{}'.format(i), end=', ')
