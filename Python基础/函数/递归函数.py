# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 10:13
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 递归函数.py
# @Software: PyCharm


# 函数自己调用自己 计算阶乘
def Fib(n):
    if n == 1:
        return 1
    else:
        return Fib(n-1) * n

print(Fib(5))



