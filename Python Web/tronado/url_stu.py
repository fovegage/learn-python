# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 11:28
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : url_stu.py
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import url, RequestHandler

define("port", default=8000, type=int, help="run server on the given port.")

class IndexHandler(RequestHandler):
    def get(self):
        python_url = self.reverse_url("python_url")
        self.write('<a href="%s">itcast</a>' %
                   python_url)

class ItcastHandler(RequestHandler):
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
            (r"/", IndexHandler),
            url(r"/python", ItcastHandler, {"subject":"python"}, name="python_url"),
            (r"/cpp", ItcastHandler, {"subject": "c++"}),
        ],
        debug = True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()