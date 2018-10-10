# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 12:09
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : header_stu.py
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import tornado.httpserver


class Indexhandle(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")
        self.set_header("gage", 'love')
        # self.set_status(404)

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', Indexhandle),
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()