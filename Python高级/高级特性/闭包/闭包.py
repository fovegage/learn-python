# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 11:23
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 闭包.py
# @Software: PyCharm

# 函数调用函数
def fun(num):
    def inner(num_in):
        return num + num_in

    return inner

a = fun(5)
print(fun(5)(10))  # 链式调用

# 函数调用类  工厂类
def class_factory():
    class Foo(object):
        def print(self):
            print(5)
    return Foo


F = class_factory()
f = F()
f.print()
print(type(f))
