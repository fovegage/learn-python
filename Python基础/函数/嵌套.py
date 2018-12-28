# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 9:52
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 嵌套.py
# @Software: PyCharm

def B():
    print('执行B函数')
    print('B函数执行完毕')

def A():
    print('我是A函数')
    B()
    print('A函数执行完毕')

A()