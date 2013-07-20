#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/peak.html
import sys
import urllib2
import pickle

PICKLE_FILE = "http://www.pythonchallenge.com/pc/def/banner.p"


def printMatrix(matrix):
    for line in matrix:
        for char, num in line:
            for x in range(0, num):
                sys.stdout.write(char)
        sys.stdout.write('\n')


# 05/05.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    p = urllib2.urlopen(PICKLE_FILE).read()
    matrix = pickle.loads(p)
    printMatrix(matrix)


if __name__ == '__main__':
    main()
