#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/channel.html
import sys
import re
import zipfile

ZIP_LOCATION = '06/channel.zip'
FILE_FORMAT = "%s.txt"
MATCHER = re.compile("Next nothing is (\d+)")


def getNothing(nothing, myzip):
    print FILE_FORMAT % nothing
    return myzip.open(FILE_FORMAT % nothing).read()


# 06/06.py 90052
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    comments = []
    nothing = args[0]
    with zipfile.ZipFile(ZIP_LOCATION) as myzip:
        text = getNothing(nothing, myzip)
        comments.append(myzip.getinfo(FILE_FORMAT % nothing).comment)
        match = MATCHER.findall(text)
        while len(match) > 0:
            text = getNothing(match[0], myzip)
            comments.append(myzip.getinfo(FILE_FORMAT % match[0]).comment)
            match = MATCHER.findall(text)
        print text
    print ''.join(comments)


if __name__ == '__main__':
    main()
