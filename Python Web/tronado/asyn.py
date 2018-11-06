# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 16:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : asyn.py
# @Software: PyCharm

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado import httpclient

from tornado.options import define, options

define('port', 5998, type=int, help='port')


class Index(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        http = httpclient.AsyncHTTPClient()
        http.fetch('http://pv.sohu.com/cityjson', callback=self.response)

    def response(self, response):
        if response.error:
            self.send_error(500)
        else:
            self.write(response.body)

        self.finish()


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[(
            r'/', Index,
        )],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
