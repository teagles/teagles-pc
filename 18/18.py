#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/balloons.html
import sys
import difflib

FIRST = '- '
SECOND = '+ '
BOTH = '  '

file1 = []
file2 = []
file3 = []

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]


def dehexify(s):
    return chr(int(s, 16))


def clean_file(s):
    return s.replace(' ', '').replace('\n', '')


# 18/18.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    text1 = open('18/delta1.txt').read().splitlines()
    text2 = open('18/delta2.txt').read().splitlines()
    for byte in difflib.ndiff(text1, text2):
        if byte.startswith(FIRST):
            file1.append(byte.replace(FIRST, ''))
        elif byte.startswith(SECOND):
            file2.append(byte.replace(SECOND, ''))
        else:
            file3.append(byte.replace(BOTH, ''))
    with open('18/file1.png', 'wb') as outfile:
        outfile.write(''.join(map(dehexify, split_len(clean_file(''.join(file1)), 2))))
    with open('18/file2.png', 'wb') as outfile:
        outfile.write(''.join(map(dehexify, split_len(clean_file(''.join(file2)), 2))))
    with open('18/file3.png', 'wb') as outfile:
        outfile.write(''.join(map(dehexify, split_len(clean_file(''.join(file3)), 2))))


if __name__ == '__main__':
    main()
