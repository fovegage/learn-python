# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 10:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : http_stu.py
# @Software: PyCharm

# 请求
import tornado.httpserver
# 监听
import tornado.ioloop
# web
import tornado.web


class IndexHandle(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")

if __name__ == '__main__':
    app = tornado.web.Application(handlers=[
        (r'/',IndexHandle),
    ])
    # listen监听
    # app.listen(8000)
    # tornado.ioloop.IOLoop.current().start()
    # http
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
    # 绑定

