# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 16:06
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : asyn.py
# @Software: PyCharm

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado import httpclient, gen

from tornado.options import define, options

define('port', 5948, type=int, help='port')


# 回调异步
class Index1(tornado.web.RequestHandler):

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

# 协程异步
class Index2(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch('http://whois.pconline.com.cn/ipJson.jsp')

        if response.error:
            self.send_error(500)
        else:
            self.write(response.body)

# 并行协程
class Index3(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        id = ['1282283', '5052594', '7471298']
        ret1, ret2 = yield [self.get_info(id[0]), self.get_info(id[1])]
        ret_dict = yield dict(ret3=self.get_info(id[2]))
        self.response(id[0], ret1)
        self.response(id[1], ret2)
        self.response(id[2], ret_dict['ret3'])

    def response(self, id, price):
        self.write(id)
        self.write(price)
        self.write('<br>')

    @gen.coroutine
    def get_info(self, id):
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch('http://p.3.cn/prices/mgets?skuIds=J_{}&type=1'.format(id))
        raise gen.Return(response.body)

if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[(
            # r'/', Index1,
            # r'/',Index2,
            r'/',Index3
        )],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
