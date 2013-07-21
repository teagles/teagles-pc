#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/oxygen.html
import sys
import Image
import re

ARRAY = re.compile("\[.*\]")
CHAR_WIDTH = 7


def greyPix(pixel):
    return pixel[0] == pixel[1] and pixel[1] == pixel[2]


def findBar(pixels, height):
    for i in range(0, height):
        if greyPix(pixels[0, i]):
            return i


def readBar(pixels, rowIndex, width):
    result = []
    for i in range(0, (width / CHAR_WIDTH)):
        if not greyPix(pixels[i * CHAR_WIDTH, rowIndex]):
            break
        pixel = pixels[i * CHAR_WIDTH, rowIndex][0]
        result.append(pixel)
    return result


def decodeStr(array):
    return ''.join(map(lambda x: str(unichr(x)), array))


# 07/07.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    im = Image.open('07/oxygen.png')
    pixels = im.load()
    rowIndex = findBar(pixels, im.size[1])
    bar = readBar(pixels, rowIndex, im.size[0])
    message = decodeStr(bar)
    print message
    print decodeStr(eval(ARRAY.search(message).group()))


if __name__ == '__main__':
    main()
