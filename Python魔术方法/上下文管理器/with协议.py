# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 14:04
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : with协议.py
# @Software: PyCharm

# 自己实现的上下文管理器
class Close():
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj  # 返回作为as目标

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except AttributeError:
            print(exc_type)


# 这是我们自定义的  上下文管理器    它自带close() 功能
with Close(int(5)) as i:
    i += 1
    print(i)


# 嵌套with

from socket import socket, SOCK_STREAM, AF_INET
from functools import partial


class connect():
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.con = []

    def __enter__(self):
        scok = socket(self.family, self.type)
        scok.connect(self.address)
        self.con.append(scok)
        return scok

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.pop().close




with connect(("www.python.org", 80)) as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))  # b'' 等待其出现
    print(resp)


# partial实现原理如下
from functools import partial

conn = connect(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
        # s1 and s2 are independent sockets