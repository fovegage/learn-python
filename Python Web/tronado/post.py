# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 16:38
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : post.py
# @Software: PyCharm

import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.options import define, options

define('port', default=8088, type=int, help='please run this port')
class Post(tornado.web.RequestHandler):

    def post(self):
        text = self.get_argument('text')
        self.write(text)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(
            r'/', Post,
        )],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
