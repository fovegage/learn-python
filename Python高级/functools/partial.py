# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 14:31
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : partial.py
# @Software: PyCharm

from functools import partial


# 函数调用的时候，有多个参数，但是其中的一个参数已经知道了，
# 我们可以通过这个参数重新绑定一个新的函数，然后去调用这个新函数
def add(a, b):
    return a + b


plus = partial(add, 100)  #

print(plus)
print(plus(9))


def add(a, b, c):
    return a + b + c


add_one = partial(add, b=1, c=3)  # 参数指定 绑定 b和c
add_two = partial(add_one, a=2)  # 由于上一步绑定了 b,c 这一步绑定了 a  即调用不需要传参数
print(add_one(a=3))  # 传入a
print(add_two())


def hello(func=None, name=None):
    if func is None:
        return partial(hello, name="Gage")


print(hello(name='hello'))
