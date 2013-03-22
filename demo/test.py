#!/usr/bin/env python
# coding: utf-8
import sniorfy.rpc
import sniorfy.ioloop


class Application(sniorfy.rpc.Application):
    def __init__(self, request_callback):
        sniorfy.rpc.Application.__init__(self, RequestHandler)


class RequestHandler(sniorfy.rpc.RequestHandler):
    def deal(self):
        print self.request.argv
        for arg in self.request.argv:
            self.appendarg(arg)


def main():
    app = Application(RequestHandler)
    app.listen(3370)
    sniorfy.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
