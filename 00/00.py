#!/usr/bin/env python
import sys

URL_PREFIX = 'http://www.pythonchallenge.com/pc/def/'
URL_SUFFIX = '.html'
START = 0


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print 'URL is: %s%d%s' % (URL_PREFIX, START, URL_SUFFIX)


if __name__ == '__main__':
    main()
