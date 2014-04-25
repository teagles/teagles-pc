#!/usr/bin/env python
# http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
import sys
import wave


# 19/19.py
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    open('19/indian.wav', 'wb').write(open('19/indian.wav.b64', 'rb'
                                           ).read().decode('base64'))
    w = wave.open('19/indian.wav', 'r')
    s = w.readframes(w.getnframes())
    ww = wave.open('19/indian-out.wav', 'w')
    ww.setnchannels(w.getnchannels())
    ww.setsampwidth(w.getsampwidth())
    ww.setframerate(w.getframerate())
    ww.writeframes(s[::-1])
    ww.close()


if __name__ == '__main__':
    main()
