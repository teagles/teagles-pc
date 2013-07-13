#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/0.html
import sys
import math

URL_PREFIX = 'http://www.pythonchallenge.com/pc/def/'
URL_SUFFIX = '.html'
START = 0


# 00/00.py 2 38
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print 'URL is: %s%d%s' % (URL_PREFIX, math.pow(int(args[0]), int(args[1])),
                              URL_SUFFIX)


if __name__ == '__main__':
    main()
