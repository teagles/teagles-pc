#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html
import sys
import requests
import Image
import ImageDraw
import functools

IMAGE_URL = 'http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif'
FNAME = '22/white.gif'


class FrameTurtle:
    def __init__(self, x, y, width, height):
        self.im_buffer = None
        self.im_draw = None
        self.def_x = x
        self.def_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, x_inc, y_inc):
        self.x = self.x + x_inc
        self.y = self.y + y_inc
        self.im_draw.point((self.x, self.y), fill='black')

    def reset(self):
        self.show()
        self.im_buffer = Image.new("RGB", (self.width, self.height), "white")
        self.im_draw = ImageDraw.Draw(self.im_buffer)
        self.x = self.def_x
        self.y = self.def_y
        self.draw(0, 0)

    T9 = {(98, 98): functools.partial(draw, x_inc=-1, y_inc=-1),
          (100, 98): functools.partial(draw, x_inc=0, y_inc=-1),
          (102, 98): functools.partial(draw, x_inc=1, y_inc=-1),
          (98, 100): functools.partial(draw, x_inc=-1, y_inc=0),
          (100, 100): reset,
          (102, 100): functools.partial(draw, x_inc=1, y_inc=0),
          (98, 102): functools.partial(draw, x_inc=-1, y_inc=1),
          (100, 102): functools.partial(draw, x_inc=0, y_inc=1),
          (102, 102): functools.partial(draw, x_inc=1, y_inc=1),
          }

    def action(self, p_x, p_y):
        FrameTurtle.T9[(p_x, p_y)](self)

    def show(self):
        if self.im_buffer is not None:
            self.im_buffer.show()


def iter_frames(im):
    try:
        i = 0
        while True:
            im.seek(i)
            yield im.load()
            i = i + 1
    except EOFError:
        pass


def action_not_black(pixels, turtle):
    for i in range(0, 200):
        for j in range(0, 200):
            if pixels[i, j] != 0:
                turtle.action(i, j)


# 22/22.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    with open(FNAME, 'wb') as f:
        f.write(requests.get(IMAGE_URL).content)
    white = Image.open(FNAME)
    turtle = FrameTurtle(100, 100, 200, 200)
    for im in iter_frames(white):
        action_not_black(im, turtle)
    turtle.show()


if __name__ == '__main__':
    main()
