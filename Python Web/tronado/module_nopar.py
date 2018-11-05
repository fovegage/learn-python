# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 11:32
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : module_nopar.py
# @Software: PyCharm

import tornado.web
import tornado.httpserver
import tornado.ioloop

from tornado.options import define, options

define('port', 7875, type=int, help='port')


class moudle(tornado.web.RequestHandler):

    def get(self):
        self.render('templates/module.html')


# 此modile  不传值
class hellomo(tornado.web.UIModule):

    def render(self):
        return '<h1>Hello, world!</h1>'

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(
            r'/', moudle,
        )],
        ui_modules={'hello':hellomo},
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
