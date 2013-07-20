#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/equality.html
import sys
import string
import re
import urllib2

SITE = "http://www.pythonchallenge.com/pc/def/equality.html"
PATTERN = "[%s]{1}[%s]{3}([%s]{1})[%s]{3}[%s]{1}" % (string.lowercase,
                                                     string.uppercase,
                                                     string.lowercase,
                                                     string.uppercase,
                                                     string.lowercase)


# 03/03.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print ''.join(re.compile(PATTERN).findall(urllib2.urlopen(SITE).read()))


if __name__ == '__main__':
    main()
