# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 14:18
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 作用域.py
# @Software: PyCharm


count = 0

def test1():
    global count  # 内部函数不可直接使用全局变量
    count += 1
    print(count)

test1()


# def test2():
#     print(count)   # 如果不修改 可以直接引用  指的是内存地址
#
# test2()
#
#
# # nonlocal 用来使用 外层非全局变量   修改后 内存地址未变  只是数据改变
# def test3():
#     num = 0
#     def test_in():
#         nonlocal num
#         num += 1
#         return num
#     return test_in
#
# def make_test():
#     mc = test3()
#     print(mc())
#     print(mc())
#     print(mc())
#
# make_test()

