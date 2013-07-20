#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/ocr.html
import sys
import urllib

SITE = "http://www.pythonchallenge.com/pc/def/ocr.html"


def isChar(x):
    if x.isalpha():
        return x
    else:
        return ''


# 02/02.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print ''.join(map(isChar, urllib.urlopen(SITE).read()))


if __name__ == '__main__':
    main()
