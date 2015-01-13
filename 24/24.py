#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/ambiguity.html
import os
import sys
import Image
import requests
import collections
import ImageDraw

IMAGE_URL = 'http://butter:fly@www.pythonchallenge.com/pc/hex/maze.png'
FNAME = '24/maze.png'

Point = collections.namedtuple('Point', ['x', 'y'])


class MazeTurtle:
    DIRECTIONS = {'north': lambda p: Point(p.x, p.y - 1),
                  'east': lambda p: Point(p.x + 1, p.y),
                  'south': lambda p: Point(p.x, p.y + 1),
                  'west': lambda p: Point(p.x - 1, p.y)}

    def __init__(self, img, start_point, goal_point, wall_colour):
        self.img = img
        self.pix = img.load()
        self.point = start_point
        self.goal_point = goal_point
        self.wall_colour = wall_colour
        self.visited = set()
        self.path = []
        self.branches = []
        self.dead_ends = []
        self.im_num = 0

    def valid_point(self, p):
        return (p.x >= 0 and p.y >= 0 and p.x < self.img.size[0]
                and p.y < self.img.size[1])

    def scout(self):
        possibilities = []
        for fp in MazeTurtle.DIRECTIONS.values():
            pp = fp(self.point)
            if self.valid_point(pp):
                if self.pix[pp] != self.wall_colour:
                    if pp not in self.visited:
                        possibilities.append(pp)
        return possibilities

    def victory(self):
        return (self.goal_point.x == self.point.x
                and
                self.goal_point.y == self.point.y)

    def find_path(self):
        while (not self.victory()):
            self.path.append(self.point)
            self.visited.add(self.point)
            possibilities = self.scout()
            if len(possibilities) > 0:
                if len(possibilities) > 1:
                    self.branches.append((len(self.path), possibilities))
                self.point = possibilities[0]
            else:
                #print self.path
                #print self.branches
                self.dead_ends.append(self.path[self.branches[-1][0]:])
                del self.path[self.branches[-1][0]:]
                del self.branches[-1][1][0]
                #self.show_path()
                #raw_input('Continue:')
                self.point = self.branches[-1][1][0]
                if len(self.branches[-1][1]) is 1:
                    del self.branches[-1]
        self.path.append(self.point)
        return self.path

    def show_path(self):
        temp = self.img.copy()
        draw = ImageDraw.Draw(temp)
        for dp in self.path:
            draw.point(dp, fill='green')
        for de in self.dead_ends[:-1]:
            for dp in de:
                #draw.point(dp, fill='blue')
                pass
        for dp in self.dead_ends[-1]:
            #draw.point(dp, fill='purple')
            pass
        temp.save('24/img%d.png' % self.im_num, quality=100)
        self.im_num = self.im_num + 1


# 24/24.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    if not os.path.isfile(FNAME):
        with open(FNAME, 'wb') as f:
            f.write(requests.get(IMAGE_URL).content)
    img = Image.open(FNAME)
    turtle = MazeTurtle(img, Point(639, 0), Point(1, 640), 25)
    print turtle.find_path()
    turtle.show_path()


if __name__ == '__main__':
    main()
