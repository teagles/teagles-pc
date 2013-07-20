#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/linkedlist.php
import sys
import re
import urllib2

SITE = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
MATCHER = re.compile("and the next nothing is (\d+)")


def getPage(nothing):
    print SITE % nothing
    return urllib2.urlopen(SITE % nothing).read()


# 04/04.py 12345
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    text = getPage(args[0])
    match = MATCHER.findall(text)
    while len(match) > 0:
        text = getPage(match[0])
        match = MATCHER.findall(text)
    print text


if __name__ == '__main__':
    main()
