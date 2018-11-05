# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:37
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : template.py
# @Software: PyCharm

import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.options import define, options
import os


define('port', default=8011, type=int, help='please run this port')
class Post(tornado.web.RequestHandler):

    def get(self):

        self.render('tem_fun.html', a = 4, list=[1, 2, 3], b='&',)

class extend(tornado.web.RequestHandler):

    def get(self):
        mailLink = '<a href="mailto:contact@burtsbooks.com">Contact Us</a>'
        self.render('show.html', title = 'show标题', mailLink= mailLink)

class auto(tornado.web.RequestHandler):

    def get(self):
        self.render('auto.html')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(
            # r'/template', Post,
            # r'/extend', extend,
            r'/auto', auto,
        )],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()