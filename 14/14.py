#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/italy.html
import sys
import Image

WIRE_PATH = '14/wire.png'
IM_DIMENSION = 100


class SpiralTurtle:
    SIDE_RULES = [{'name': 'right',
                   'increment': (1, 0),
                   'line': lambda itr, dim: dim - itr * 2},
                  {'name': 'down',
                   'increment': (0, 1),
                   'line': lambda itr, dim: dim - itr * 2 - 1},
                  {'name': 'left',
                   'increment': (-1, 0),
                   'line': lambda itr, dim: dim - itr * 2 - 1},
                  {'name': 'up',
                   'increment': (0, -1),
                   'line': lambda itr, dim: dim - itr * 2 - 2}]

    def __init__(self, x, y, source):
        self.output = Image.new("RGB", (x, y))
        self.source = source
        self.i = -1
        self.j = 0
        self.index = 0
        self.itr = 0

    def walk(self):
        while self.index < len(self.source):
            cur_side = SpiralTurtle.SIDE_RULES[self.itr % 4]
            # print 'range %s' % (range(0, cur_side['line'](self.itr / 4,
            #                                               self.output.size[0])))
            for lin_index in range(0, cur_side['line'](self.itr / 4,
                                                       self.output.size[0])):
                self.i += cur_side['increment'][0]
                self.j += cur_side['increment'][1]
                # print '%i,%i' % (self.i, self.j)
                self.output.load()[self.i, self.j] = self.source[self.index]
                self.index += 1
            self.itr += 1


# 14/14.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    walker = SpiralTurtle(IM_DIMENSION, IM_DIMENSION,
                          Image.open(WIRE_PATH).getdata())
    walker.walk()
    walker.output.show()


if __name__ == '__main__':
    main()
