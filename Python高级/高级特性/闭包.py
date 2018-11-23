# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 11:23
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 闭包.py
# @Software: PyCharm

def fun(num):
    def inner(num_in):
        return num + num_in

    return inner

a = fun(5)
print(fun(5)(10))