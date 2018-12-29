# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 10:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 返回值.py
# @Software: PyCharm

# 两个返回值将用元组接受

def div(a, b):
    return a // b, a % b

x, y = div(9, 4)
print(x, y)