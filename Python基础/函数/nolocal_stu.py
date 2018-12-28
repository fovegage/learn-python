# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 14:18
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 作用域.py
# @Software: PyCharm


# nonlocal 用来使用 外层非全局变量   修改后 内存地址未变  只是数据改变
def test3():
    num = 0
    def test_in():
        nonlocal num
        num += 1
        return num
    return test_in

def make_test():
    mc = test3()
    print(mc())
    print(mc())
    print(mc())

make_test()

