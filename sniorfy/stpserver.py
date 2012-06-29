#!/usr/bin/python
# coding: utf-8
import socket
from sniorfy.ioloop.netutil import TCPServer


class STPServer(TCPServer):
    def __init__(self, request_callback, io_loop=None, application=None, **kwargs):
        self.request_callback = request_callback
        self.application = application
        TCPServer.__init__(self, io_loop=io_loop, **kwargs)

    def handle_stream(self, stream, address):
        STPConnection(stream, address, self.request_callback, self.application)


class STPConnection(object):
    def __init__(self, stream, address, request_callback, application):
        self.stream = stream
        self.application = application
        if self.stream.socket.family not in (socket.AF_INET, socket.AF_INET6):
            # Unix (or other) socket; fake the remote address
            address = ('0.0.0.0', 0)
        self.address = address
        self.request_callback = request_callback
        self._request = STPRequest(self)
        self._request_finished = False
        self.read_arg()

    def read_arg(self):
        self.stream.read_until(b'\r\n', self._on_arglen)

    def _on_arglen(self, data):
        if data == '\r\n':
            self.request_callback(self._request)
            self._request = STPRequest(self)
            self.read_arg()
        else:
            try:
                arglen = int(data[:-2])
            except Exception as e:
                raise e
            self.stream.read_bytes(arglen, self._on_arg)

    def _on_arg(self, data):
        self._request.add_arg(data)
        self.stream.read_until(b'\r\n', self._on_strip_arg_endl)

    def _on_strip_arg_endl(self, data):
        self.read_arg()


class STPRequest(object):
    def __init__(self, connection):
        self._argv = []
        self.connection = connection

    def add_arg(self, arg):
        self._argv.append(arg)

    @property
    def argv(self):
        return self._argv
