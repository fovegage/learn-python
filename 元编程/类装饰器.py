# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 18:31
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 类装饰器.py
# @Software: PyCharm

from functools import wraps


class A():
    def decorate1(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print('1')
            return func(*args, **kwargs)
        return wrap

    @classmethod
    def decorate2(cls, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            print('2')
            return func(*args, **kwargs)

        return wrap


a = A()
a.decorate1
def add():
    return 'inner'

print(add())


A.decorate2
def sub():
    return 'sub'


print(sub())