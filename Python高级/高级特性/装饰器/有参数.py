# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 有参数.py
# @Software: PyCharm

# 有参数
def A(fun):
    def A_in(a, b):
        fun(a, b)
        return a*b
    return A_in

@A
def B(a, b):
    print(a+b)

print(B(3, 4))