# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 11:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 有参数.py
# @Software: PyCharm

# 有参数
def A(fun):  # 函数传入
    def A_in(a, b):  # 参数进入
        fun(a, b)   # 执行传入的

        return fun(a, b)
        # return a * b
    return A_in  # 返出内部执行结果

@A
def B(a, b):
    return (a+b)

print(B(3, 4))