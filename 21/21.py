#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg
# 'Range': 'bytes=1152983631-30347'
# Password: redavni
import sys
import bz2
import zlib

COMPRESSION_LIBS = {'x\x9c': zlib.decompress,
                    'BZh': bz2.decompress}


def identify(data):
    for header in COMPRESSION_LIBS:
        if data.startswith(header):
            return (COMPRESSION_LIBS[header], False)
        elif data.endswith(header[::-1]):
            return (COMPRESSION_LIBS[header], True)
    return (None, None)


def unpack(data, library, reversed):
    if reversed:
        return library(data[::-1])
    else:
        return library(data)


def dot_matrix(library, reversed):
    if reversed:
        sys.stdout.write('\n')
    if library is zlib.decompress:
        sys.stdout.write('X')
    else:
        sys.stdout.write('0')


# 21/21.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    with open('21/package.pack', 'rb') as f:
        package = f.read()
    library, reversed = identify(package)
    dot_matrix(library, reversed)
    while (library is not None):
        dot_matrix(library, reversed)
        package = unpack(package, library, reversed)
        library, reversed = identify(package)
    with open('21/out.data', 'wb') as f:
        f.write(package)


if __name__ == '__main__':
    main()
