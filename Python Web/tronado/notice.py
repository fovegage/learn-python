# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.options import define, options

define('port', default=26459, type=int, help='please run this port')
class Post(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        name = self.get_argument('type')
        print(name)
        self.write({"code":0,"msg":"success"})
        if name == 'TRADE_ORDER_STATE':
            self.write('hello')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(
            r'/notice', Post,
        )],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
