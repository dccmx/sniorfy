#!/usr/bin/env  python
# coding: utf-8
import sniorfy.magicserver
import sys
import time
import logging
logging.basicConfig(level=logging.INFO)


class MyServer(sniorfy.magicserver.MagicServer):
    def func1(self, handler, args):
        logging.info('call func1')
        for arg in args:
            handler.appendarg(arg)

    def long(self, handler, args):
        logging.info('call long')
        time.sleep(2)
        for arg in args:
            handler.appendarg(arg)

    def func2(self, handler, args):
        logging.info('call func2')
        for arg in args:
            handler.appendarg(arg)

    def ping(self, handler, args):
        logging.info('call ping')
        handler.appendarg('PONG')


def main():
    server = MyServer(int(sys.argv[1]))
    server.start()


if __name__ == '__main__':
    main()
