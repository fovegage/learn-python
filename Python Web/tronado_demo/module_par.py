# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 14:24
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : module_par.py
# @Software: PyCharm

import tornado.web
import tornado.httpserver
import tornado.ioloop

from tornado.options import define, options

define('port', 7874, type=int, help='port')


class moudle(tornado.web.RequestHandler):

    def get(self):
        self.render('templates/mod/index.html',books=[
            {'title':'gage', 'image':'lll'},
            {'title':'manli', 'image': 'ddd'}

        ])


# 此modile  不传值
class hellomo(tornado.web.UIModule):

    def render(self, book):
        return self.render_string('templates/mod/book.html', book=book)

    def embedded_javascript(self):
        return "document.write(\"hi!\")"

    def embedded_css(self):
        return ".book {background-color:#F5F5F5}"

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