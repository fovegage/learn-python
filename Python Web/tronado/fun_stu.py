# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 14:59
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : fun_stu.py
# @Software: PyCharm
import tornado.ioloop
import tornado.web
import tornado.httpserver

import os

# 自定义函数
def title_join(title):
    return "hahaha".join(title)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        house_info = {
            "price": 398,
            "title": "宽窄巷子+160平大空间+文化保护区双地铁",
            "score": 55,
            "comments": 6,
            "position": "北京市丰台区六里桥地铁",
            "text":'<script>alert("hello!");</script>'
        }
        self.render("fun.html", **house_info, t = title_join)


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
        ],
        template_path = os.path.join(os.path.dirname(__file__), 'templates'),
        debug=True,
        autoescape=None,  # 关闭自动转义
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9008)
    tornado.ioloop.IOLoop.instance().start()