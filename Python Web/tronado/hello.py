# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 16:19
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : hello.py
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

define('port', default=8008, type=int, help='Please run this port')
class Hello(tornado.web.RequestHandler):

    def get(self):
        self.write('hello')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(
            r'/', Hello,
        )],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
