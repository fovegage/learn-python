# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 14:11
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 单例模式.py
# @Software: PyCharm


class Sing(str):

    def __new__(cls, word):
        return str.__new__(cls, word)

print(id(Sing('Hello')))
print(id(Sing('Kill')))
# 所谓单列模式就是 公用一个  因此他的内存地址是一样的  且 __init__ 只调用一次
class Single(object):

    __isstance = None

    def __new__(cls, name, age):
        if not cls.__isstance:
            cls.__isstance = object.__new__(cls)
        return cls.__isstance

a = Single('Gage', 18)
b = Single('Fovegage', 20)
print(id(a))
print(id(b))
print(a)