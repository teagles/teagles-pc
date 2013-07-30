#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
import sys
import Image

MAGIC_COLOUR = 195
IMAGE_PATH = '16/mozart.gif'


class Straightener:
    def __init__(self, source_image):
        self.s_im = source_image
        self.s_pix = source_image.load()
        self.d_im = source_image.copy()
        self.d_pix = self.d_im.load()

    def find_first_magic(self, row_index):
        for i in range(0, self.s_im.size[0]):
            if self.s_pix[i, row_index] is MAGIC_COLOUR:
                return i
        return 0

    def straighten(self):
        for j in range(0, self.s_im.size[1]):
            offset = self.find_first_magic(j)
            modulo = self.s_im.size[0]
            for i in range(0, modulo):
                self.d_pix[i, j] = self.s_pix[(i + offset) % modulo, j]
        self.d_im.show()


# 16/16.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    s = Straightener(Image.open(IMAGE_PATH))
    s.straighten()


if __name__ == '__main__':
    main()
