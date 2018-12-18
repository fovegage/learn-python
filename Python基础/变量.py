# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 14:46
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 变量.py
# @Software: PyCharm


# 何为可修改类型  即   修改后  内存地址不变
a = 100

def math():
    # global a
    # a += 1   修改需要使用  global  使用后 函数数据指向为修改的值   内存地址不变  指向改变
    print(a)  # 可以直接使用全局变量  在函数内部  而不可修改


def samp():

    a = 300  # 这里并不是修改全局变量    内部的 a 和  外部的 a 只是名字一样罢了  但内存地址是不一样的
    print(a)

samp()

