# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 13:45
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : static_stu.py
# @Software: PyCharm

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os

from tornado.options import define, options
define('port', default=9000, help="run")

class FirstHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class Showhandle(tornado.web.RequestHandler):
    def post(self):
        n1 = self.get_argument('noun1')
        n2 = self.get_argument('noun2')
        vb = self.get_argument('verb')
        n3 = self.get_argument('noun3')
        self.render('show.html', roads = n1, wood = n2, made = vb, difference = n3)


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', FirstHandle),
            (r'/poem', Showhandle)
        ],
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), 'static'),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()