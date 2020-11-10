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
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self, *args, **kwargs):
        self.set_header("Content-Type", "text/plain")
        self.write(self.get_argument('message') + str(self.request.headers) + str(self.request.arguments))

class Num(tornado.web.RequestHandler):

    # 传参方式
    def get(self, num):
        self.write("You requested the story " + num)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', Hello),
            (r'/num/([0-9]+)', Num),
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
