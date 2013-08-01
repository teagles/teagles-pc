#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/romance.html
import sys
import re
import requests
import urllib
import bz2

SITE = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"
MATCHER = re.compile("and the next busynothing is (\d+)")
INFO = []

def getPage(nothing):
    # print SITE % nothing
    page = requests.get(SITE % nothing)
    text = page.text
    # print text
    # print page.cookies['info']
    cookie = urllib.unquote_plus(page.cookies['info'])
    # print cookie
    INFO.append(cookie)
    return text


# 17/17.py 12345
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    text = getPage(args[0])
    match = MATCHER.findall(text)
    while len(match) > 0:
        text = getPage(match[0])
        match = MATCHER.findall(text)
    # print text
    print bz2.decompress(''.join(INFO))


if __name__ == '__main__':
    main()
