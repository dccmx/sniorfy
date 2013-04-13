#!/usr/bin/env  python
# coding: utf-8
import sniorfy.magicserver
import sys
import time


class MyServer(sniorfy.magicserver.MagicServer):
    def func1(self, handler, args):
        for arg in args:
            handler.appendarg(arg)

    def func2(self, handler, args):
        for arg in args:
            handler.appendarg(arg)

    def ping(self, handler, args):
        time.sleep(2)
        handler.appendarg('PONG')


def main():
    server = MyServer(int(sys.argv[1]))
    server.start()


if __name__ == '__main__':
    main()
