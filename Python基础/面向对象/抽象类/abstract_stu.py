# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 15:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : abstract_stu.py
# @Software: PyCharm

# abstractmethod  定义为接口 必须有实现类
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('实现类')

s = SocketStream()
s.read()

# 我们也可以注册使用

import io
IStream.register(io.IOBase)
f = open('E:\\test.txt')
print(isinstance(f, IStream))