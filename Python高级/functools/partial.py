# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 14:31
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : partial.py
# @Software: PyCharm

from functools import partial

# 函数调用的时候，有多个参数 参数，但是其中的一个参数已经知道了，
# 我们可以通过这个参数重新绑定一个新的函数，然后去调用这个新函数
def add(a, b):
    return a + b

plus =partial(add, 100)  #

print(plus(9))