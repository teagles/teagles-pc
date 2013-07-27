#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/uzi.html
import sys
import calendar
import re

MONTH = 1
DAY = 26
TARGET_DAY_OF_WEEK = 0
TARGET_YEAR_PATTERN = re.compile('1\d+6$')


# 15/15.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if len(args) != 1:
        year = 2013
    else:
        year = eval(args[0])
    while year > 0:
        if TARGET_YEAR_PATTERN.match(str(year)):
            if calendar.weekday(year, MONTH, DAY) == TARGET_DAY_OF_WEEK:
                print '%i' % year
        year -= 1


if __name__ == '__main__':
    main()
