#!/usr/bin/env  python
# coding: utf-8
import sniorfy.magicserver


class MyServer(sniorfy.magicserver.MagicServer):
    def func1(self, handler, args):
        for arg in args:
            handler.addarg(arg)

    def func2(self, handler, args):
        for arg in args:
            handler.addarg(arg)

    def ping(self, handler, args):
        handler.addarg('pong')


def main():
    server = MyServer(3370)
    server.start()


if __name__ == '__main__':
    main()
