#!/usr/bin/python
# coding: utf-8
import sniorfy.rpc
import sniorfy.ioloop


class Application(sniorfy.rpc.Application):
    def __init__(self, server, request_callback):
        self.server = server
        sniorfy.rpc.Application.__init__(self, MagicHandler)


class MagicHandler(sniorfy.rpc.RequestHandler):
    def deal(self):
        argv = self.request.argv
        try:
            fn = getattr(self.request.connection.application.server, argv[0])
        except AttributeError:
            fn = None
        if fn is not None:
            self.appendarg('OK')
            fn(self, argv[1:])
        else:
            self.appendarg('ERR')
            self.appendarg('No such method on server')


class MagicServer(object):
    def __init__(self, port, address=''):
        self.app = Application(self, MagicHandler)
        self.app.listen(port)

    def start(self):
        sniorfy.ioloop.IOLoop.instance().start()
