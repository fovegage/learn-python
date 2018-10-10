# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 10:28
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : post_get.py
# @Software: PyCharm

import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        # text = self.get_query_arguments('text')
        # text = self.get_query_argument('text')
        self.write(text)

class Json(tornado.web.RequestHandler):
    def get(self):
        info = {
            'name':"Gage",
            'age':23,


        }
        self.write(info)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap", WrapHandler),
            (r'/json', Json)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    # 监听
    http_server.listen(options.port)
    # 线程
    tornado.ioloop.IOLoop.instance().start()