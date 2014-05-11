#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/idiot2.html
import sys
import requests
import StringIO
import zipfile

URL = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'


# 20/20.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    resp = requests.get(URL, headers={'Range': 'bytes=30203-2123456788'})
    print resp.content
    # "Why don't you respect my privacy?\n"
    print resp.headers['content-range']
    # 'content-range': 'bytes 30203-30236/2123456789'
    resp = requests.get(URL, headers={'Range': 'bytes=30237-2123456788'})
    print resp.content
    # 'we can go on in this way for really long time.\n'
    print resp.headers['content-range']
    # 'content-range': 'bytes 30237-30283/2123456789'
    resp = requests.get(URL, headers={'Range': 'bytes=30284-2123456788'})
    print resp.content
    # 'stop this!\n'
    print resp.headers['content-range']
    # 'content-range': 'bytes 30284-30294/2123456789'
    resp = requests.get(URL, headers={'Range': 'bytes=30295-2123456788'})
    print resp.content
    # 'invader! invader!\n'
    print resp.headers['content-range']
    # 'content-range': 'bytes 30295-30312/2123456789'
    resp = requests.get(URL, headers={'Range': 'bytes=30313-2123456788'})
    print resp.content
    # 'ok, invader. you are inside now. \n'
    print resp.headers['content-range']
    # 'content-range': 'bytes 30313-30346/2123456789'
    resp = requests.get(URL, headers={'Range': 'bytes=30347-2123456788'})
    print resp.content
    # ''
    resp = requests.get(URL, headers={'Range': 'bytes=2123456788-30347'})
    print resp.content
    # 'esrever ni emankcin wen ruoy si drowssap eht\n'
    print resp.content[::-1]
    # '\nthe password is your new nickname in reverse'
    print resp.headers['content-range']
    # 'content-range': 'bytes 2123456744-2123456788/2123456789'
    resp = requests.get(URL, headers={'Range': 'bytes=2123456743-30347'})
    print resp.content
    # 'and it is hiding at 1152983631.\n'
    print resp.headers['content-range']
    # 'content-range': 'bytes 2123456712-2123456743/2123456789'
    resp = requests.get(URL, headers={'Range': 'bytes=2123456711-30347'})
    print resp.content
    # ''
    resp = requests.get(URL, headers={'Range': 'bytes=1152983631-30347'})
    print resp.headers['content-range']
    # 'content-range': 'bytes 1152983631-1153223363/2123456789'
    zip_data = StringIO.StringIO(resp.content)
    with zipfile.ZipFile(zip_data) as zf:
        zf.extractall(path='21', pwd=('invader'[::-1]))


if __name__ == '__main__':
    main()
