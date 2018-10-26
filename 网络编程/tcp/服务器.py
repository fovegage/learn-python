# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 14:59
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 服务器.py
# @Software: PyCharm


from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()