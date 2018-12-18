# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 10:17
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 类方法和静态方法.py
# @Software: PyCharm

from functools import wraps
import time

def time_decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return f
    return wrapper

class Spam():
    @time_decorate
    def instance_method(self, n):
        print(self, n)
        while n>0:
            n -= 1

    @classmethod
    @time_decorate
    def class_method(cls, n):
        print(cls, n)
        while n>0:
            n -= 1

    @staticmethod
    @time_decorate
    def static_method(n):
        print(n)
        while n>0:
            n -= 0

s = Spam()
s.instance_method(100000000)

Spam.class_method(100000000)   # 类方法和自定义装饰器不可互换

Spam.static_method(100000000)