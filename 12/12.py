#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/evil.html
# http://www.garykessler.net/library/file_sigs.html
import sys
# import Image

DATA = '12/evil2.gfx'
PATH_PREFIX = '12/decoded-evil%i.%s'
FILE_EXTENSIONS = {'\xff': 'jpg', '\x89': 'png', 'G': 'gif'}


# 12/12.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    data = open(DATA, 'rb').read()
    for i in range(0, 5):
        imData = data[i::5]
        imName = PATH_PREFIX % (i, FILE_EXTENSIONS[imData[0]])
        with open(imName, 'wb') as imFile:
            imFile.write(imData)
            # Image.open(imName).show()


if __name__ == '__main__':
    main()
