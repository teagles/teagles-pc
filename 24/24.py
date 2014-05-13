#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html
import os
import sys
import requests

IMAGE_URL = 'http://butter:fly@www.pythonchallenge.com/pc/hex/maze.png'
FNAME = '24/maze.png'


# 24/24.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not os.path.isfile(FNAME):
        with open(FNAME, 'wb') as f:
            f.write(requests.get(IMAGE_URL).content)


if __name__ == '__main__':
    main()
