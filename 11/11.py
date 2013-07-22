#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/5808.html
import sys
import Image


# 11/11.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    im1 = Image.open('11/cave.jpg')
    im1pix = im1.load()
    im2 = Image.new("RGB", im1.size)
    im2pix = im2.load()
    for i in range(0, im1.size[0]):
        for j in range(0, im1.size[1]):
            if (i + j) % 2 == 0:
                im2pix[i, j] = im1pix[i, j]
    im2.show()


if __name__ == '__main__':
    main()
