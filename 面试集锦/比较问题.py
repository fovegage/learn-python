# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 17:43
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 比较问题.py
# @Software: PyCharm

import copy

# is 比较的是内存地址   == 比较内容和数据类型
a = [1, 2, 3]
b = a
print(a is b)
print(a == b)

c = copy.deepcopy(a)
print(a is c)
print(a == c)



def num(n):
    n = n + n
    print(n)

x = [1, 2]
num(x)
print(x)


