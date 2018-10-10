# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 16:12
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : user_stu.py
# @Software: PyCharm
import tornado.ioloop
import tornado.web
import tornado.httpserver
import os

class IndexHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('i.html')

class UserHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        username = self.get_argument('name')
        if username == 'hello':
            return username
        else:
            return self.redirect('/')

    @tornado.web.authenticated
    def get(self):
        self.write("登录成功")

class LoginHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandle),
            (r'/handle', UserHandler),
            (r'/login', LoginHandle)
        ],
        login_url = "/login",
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        xsrf_cookies=True, # 跨站攻击
        debug=True,
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9008)
    tornado.ioloop.IOLoop.instance().start()