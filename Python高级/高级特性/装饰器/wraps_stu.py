# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 11:19
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : wraps_stu.py
# @Software: PyCharm

from functools import wraps


#Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），
# 为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，
#最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging

@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)  # prints 'f'
print(f.__doc__)  # prints 'does some math'
print(f(5))
