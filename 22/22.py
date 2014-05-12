#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html
import sys
import requests
import Image
#import ImageDraw

IMAGE_URL = 'http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif'
FNAME = '22/white.gif'
#idraw = Image.new("RGB", (200, 200), "white")
#draw = ImageDraw.Draw(idraw)
T9 = {(98, 98): '1',
      (100, 98): '2',
      (102, 98): '3',
      (98, 100): '4',
      (100, 100): '5',
      (102, 100): '6',
      (98, 102): '7',
      (100, 102): '8',
      (102, 102): '9',
      }


def iter_frames(im):
    try:
        i = 0
        while True:
            im.seek(i)
            yield im.load()
            i = i + 1
    except EOFError:
        None


def count_not_black(pixels):
    count = 0
    for i in range(0, 200):
        for j in range(0, 200):
            if pixels[i, j] != 0:
                #print pixels[i, j]
                #draw.point((i, j), fill='black')
                #print '(%d,%d)' % (i, j)
                sys.stdout.write(T9[(i, j)])
                count = count + 1
    return count


# 22/22.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    with open(FNAME, 'wb') as f:
        f.write(requests.get(IMAGE_URL).content)
    white = Image.open(FNAME)
    for im in iter_frames(white):
        count_not_black(im)
    #idraw.show()


if __name__ == '__main__':
    main()
