# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 19:34
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : get_stu.py
# @Software: PyCharm


# 当实例被调用 会默认调用  __get__ 方法
class Inter():

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('must int')
        instance.__dict__[self.name] = value

    # 执行完释放  析构
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point():
    x = Inter('x')
    y = Inter('y')

    def __init__(self,x ,y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
# p.x = 2.5