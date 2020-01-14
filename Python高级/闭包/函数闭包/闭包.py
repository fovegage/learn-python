# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 11:23
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 闭包.py
# @Software: PyCharm

"""
介绍
def 套 def
def 套 class
的情况

"""


# 函数调用函数
def fun(num):
    """
    fun 返回 inner函数
    1、print(fun)  <function fun at 0x0000021D68BDC1E0>  fun 返回的是inner函数地址
    2、a = fun(5) num 传入
    3、a(13)  num_in 传入
    :param num:
    :return:
    """

    def inner(num_in):
        return num + num_in

    return inner


a = fun(5)
print(a(18))
print(fun(5)(10))  # 链式调用


# print('#'*10)
# 函数调用类  工厂类
# 原理一样与 def 套 def
def class_factory():
    class Foo(object):
        def print(self):
            print(1)

    class Bar:
        def print(self):
            print(2)

    return Foo


F = class_factory()
f = F()
f.print()
print(type(f))
