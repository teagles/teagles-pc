#!/usr/bin/env python
# http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
import sys
import xmlrpclib

URL = 'http://www.pythonchallenge.com/pc/phonebook.php'


# 13/13.py Bert
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    s = xmlrpclib.ServerProxy(URL)
    print s.phone(args[0])


if __name__ == '__main__':
    main()
