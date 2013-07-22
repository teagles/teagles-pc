#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/bull.html
import sys
import itertools


def groups(str):
    return [list(g) for k, g in itertools.groupby(str)]


def newTokens(str):
    for group in groups(str):
        yield '%i%s' % (len(group), group[0])


def seeNSay(str):
    return ''.join(newTokens(str))


def series(num):
    str = "1"
    for i in range(0, num):
        str = seeNSay(str)
    return str


# 10/10.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print len(series(30))


if __name__ == '__main__':
    main()
