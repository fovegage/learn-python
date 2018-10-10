# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 13:11
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : prepare_stu.py
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import tornado.httpserver
import json

class IndexHandle(tornado.web.RequestHandler):
    def prepare(self):
        if str(self.request.headers.get("Content-Type")).startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    def get(self):
        info = {
            'name':'gage'
        }
        j = json.dumps(info)
        self.write(j)

    def post(self):
        if self.json_dict:
            for key, value in self.json_dict.items():
                self.write("<h3>%s</h3><p>%s</p>" % (key, value))

    def put(self):
        if self.json_dict:
            for key, value in self.json_dict.items():
                self.write("<h3>%s</h3><p>%s</p>" % (key, value))


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandle),
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8001)
    tornado.ioloop.IOLoop.instance().start()