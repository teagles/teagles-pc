#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/idiot2.html
import sys
import requests


# 20/20.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=30203-2123456788'})
    # "Why don't you respect my privacy?\n"
    # 'content-range': 'bytes 30203-30236/2123456789'
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=30237-2123456788'})
    # 'we can go on in this way for really long time.\n'
    # 'content-range': 'bytes 30237-30283/2123456789'
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=30284-2123456788'})
    # 'stop this!\n'
    # 'content-range': 'bytes 30284-30294/2123456789'
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=30295-2123456788'})
    # 'invader! invader!\n'
    # 'content-range': 'bytes 30295-30312/2123456789'
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=30313-2123456788'})
    # 'ok, invader. you are inside now. \n'
    # 'content-range': 'bytes 30313-30346/2123456789'
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=30347-2123456788'})
    # ''
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=2123456788-30347'})
    # 'esrever ni emankcin wen ruoy si drowssap eht\n'
    # '\nthe password is your new nickname in reverse'
    # 'content-range': 'bytes 2123456744-2123456788/2123456789'
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=2123456743-30347'})
    # 'and it is hiding at 1152983631.\n'
    # 'content-range': 'bytes 2123456712-2123456743/2123456789'
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=2123456711-30347'})
    # ''
    resp = requests.get('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range':'bytes=1152983631-30347'})
    # 'content-range': 'bytes 1152983631-1153223363/2123456789'
    with open('20/data.zip', 'wb') as f:
        f.write(resp.content)


if __name__ == '__main__':
    main()
