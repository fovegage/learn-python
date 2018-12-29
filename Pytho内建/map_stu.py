# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 16:21
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : map_stu.py
# @Software: PyCharm

# 普通
# [func, iterable]  需要传入一个函数和一个可迭代对象
# 为了节约内存 map 只返回一个对象
def fun(x):
    return x * x
print(list(map(fun, [1, 2, 3])))

# lambda
print(list(map(lambda x: x*x, [1, 2, 3])))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))