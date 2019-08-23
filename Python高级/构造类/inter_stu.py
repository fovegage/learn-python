# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 12:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : inter_stu.py
# @Software: PyCharm

# __dict__ 用来存储 类内的方法或属性

class Interger():
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('must int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del self.__dict__[self.name]


class Point():
    x = Interger('x')
    y = Interger('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)



