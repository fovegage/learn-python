# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 9:24
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : args_stu.py
# @Software: PyCharm

# Python中*args和**kwargs的区别

# 不管填入几个 都是元组
def fun1(*args):
    print(args, type(args))

fun1(5)
fun1(3, 5)
# (5,) <class 'tuple'>
# (3, 5) <class 'tuple'>

# 不管填入几个 都是字典
def fun2(**kwargs):
    print(kwargs, type(kwargs))

fun2(a = 1)
fun2(a = 1, b = 2)
# {'a': 1} <class 'dict'>
# {'a': 1, 'b': 2} <class 'dict'>

# 综合 注意输出顺序
def fun3(el, *args, **kwargs):
    print(el, args, kwargs)

fun3(1, 2, 3, 4, a=5, b=6)
# 1 (2, 3, 4) {'a': 5, 'b': 6}