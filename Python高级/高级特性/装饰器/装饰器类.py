# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 19:26
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 装饰器类.py
# @Software: PyCharm
import types
from functools import wraps


class Profile():
    def __init__(self, func):
        wraps(func)(self)   # 将被包装函数的元信息复制到可调用实例中去
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profile
def add(x, y):
    return x+y

print(add(2,4))
print(add(4,4))
print(add.ncalls)

class Spam():
    @Profile
    def bar(self, a):
        print(self, a)

s = Spam()
s.bar(6)

# class hello():
#     def a(self):
#         print(self)
#
# h = hello()
# h.a()