# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 14:11
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 单例模式.py
# @Software: PyCharm


class Sing(str):

    def __new__(cls, word):
        return str.__new__(cls, word)


# print(id(Sing('Hello')))
# print(id(Sing('Kill')))
# 所谓单列模式就是 公用一个  因此他的内存地址是一样的  且 __init__ 只调用一次

# not None 为True
class Single(object):
    __isstance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__isstance:
            cls.__isstance = object.__new__(cls)
        return cls.__isstance


a = Single('a')
b = Single('b')
print(id(a))
print(id(b))

# 使用装饰器
from functools import wraps


def decorate(cls):
    instances = {}

    @wraps(cls)
    def wrapped(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapped


@decorate
class Hello:
    def __init__(self, a):
        self.a = a

    def print(self):
        print(self.a)


h1 = Hello('hello')
print(h1.print())

h2 = Hello('Gage')
print(h2.print())
