#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/integrity.html
import sys
import bz2

UN = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M' \
     '\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
PW = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9' \
     '\x14\xe1BBP\x91\xf08'


# 08/08.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print 'Username: %s' % bz2.decompress(UN)
    print 'Password: %s' % bz2.decompress(PW)


if __name__ == '__main__':
    main()
