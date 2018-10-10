# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 15:50
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : cookie_stu.py
# @Software: PyCharm

import tornado.ioloop
import tornado.web
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie('G1','hello', path='/ha')
        self.set_cookie("G2", 'j', expires_days=20)
        self.set_secure_cookie('G3', 'o')
        l = self.get_cookie('G1')
        self.write(l)

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
        ],
        cookie_secret="2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
        xsrf_cookies=True, # 跨站攻击
        debug=True,
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9008)
    tornado.ioloop.IOLoop.instance().start()