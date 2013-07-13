#!/usr/bin/env python
#http://www.pythonchallenge.com/pc/def/map.html
import sys
from string import maketrans

INCHARS = 'abcdefghijklmnopqrstuvwxyz'
OUTCHARS = 'cdefghijklmnopqrstuvwxyzab'


# 01/01.py "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc
# dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
# sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# 01/01.py map
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print args[0].translate(maketrans(INCHARS, OUTCHARS))


if __name__ == '__main__':
    main()
